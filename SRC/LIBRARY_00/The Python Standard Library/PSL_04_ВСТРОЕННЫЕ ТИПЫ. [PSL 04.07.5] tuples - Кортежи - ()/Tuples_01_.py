#------------------------------------------
# Tuples_01_ ():
#------------------------------------------
def Tuples_01_ ():
    """Tuples_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Tuples_01_.__name__}')
    print (f'#-----------------------------')

    # Устройство tuple
    # Начнем со структуры данных PyTupleObject, которая представляет собой внутреннее устройство tuple в CPython. Структура довольно простая:
    #
    # typedef struct {
    #     PyObject_VAR_HEAD
    #     /* ob_item contains space for 'ob_size' elements.
    #        Items must normally not be NULL, except during construction when
    #        the tuple is not yet visible outside the function that builds it. */
    #     PyObject *ob_item[1];
    # } PyTupleObject;
    # По сути тут у нас просто массив объектов, которые хранит tuple в ob_item. Но где же сам размер кортежа? А вот он хранится в PyObject_VAR_HEAD. В CPython есть два типа C-шных структур: с постоянным размером (как int с python3.11+) и с переменным (variable) размером. PyObject_HEAD и PyObject_VAR_HEAD соответственно. Сравним их!
    #
    # #define PyObject_HEAD PyObject ob_base;
    # #define PyObject_VAR_HEAD PyVarObject ob_base;
    # Где PyObject ob_base будет сразу хранить тип объекта, а PyVarObject ob_base будет делать так:
    #
    # typedef struct {
    #     PyObject ob_base;
    #     Py_ssize_t ob_size; /* Number of items in variable part */
    # } PyVarObject;
    # Рядом еще будет лежать и длина объекта. Следовательно, получить длину мы всегда можем за O(1), вот как выглядит __len__ кортежа:
    #
    # static Py_ssize_t
    # tuple_length(PyObject *self)
    # {
    #     PyTupleObject *a = _PyTuple_CAST(self);
    #     return Py_SIZE(a);
    # }
    # Где Py_SIZE – просто получает значение из ob_size
    #
    # static inline Py_ssize_t Py_SIZE(PyObject *ob) {
    #     return _PyVarObject_CAST(ob)->ob_size;
    # }
    # Аллокация и деаллокация
    # Все мы знаем, что tuple – объект иммутабельный 🌚️️. А значит – при любом изменении придется пересоздавать новый tuple. Кажется, что тут можно было бы оптимизировать процесс пересоздания. Давайте разбираться, как на самом деле работает создание и уничтожение кортежей. А про иммутабельность – разберем в следующей главе.
    #
    # Начнем с tp_alloc: выделение памяти под кортеж и его создание. Для создания кортежа нам потребуется только указание длины:
    #
    # static PyTupleObject *
    # tuple_alloc(Py_ssize_t size)
    # {
    #     if (size < 0) {
    #         PyErr_BadInternalCall();
    #         return NULL;
    #     }
    #     assert(size != 0);    // The empty tuple is statically allocated.
    #     Py_ssize_t index = size - 1;
    #     if (index < PyTuple_MAXSAVESIZE) {  // 20
    #         PyTupleObject *op = _Py_FREELIST_POP(PyTupleObject, tuples[index]);
    #         if (op != NULL) {
    #             return op;
    #         }
    #     }
    #     /* Check for overflow */
    #     if ((size_t)size > ((size_t)PY_SSIZE_T_MAX - (sizeof(PyTupleObject) -
    #                 sizeof(PyObject *))) / sizeof(PyObject *)) {
    #         return (PyTupleObject *)PyErr_NoMemory();
    #     }
    #     return PyObject_GC_NewVar(PyTupleObject, &PyTuple_Type, size);
    # }
    # Здесь много всего интересного:
    #
    # Создать кортеж с длиной <0 – очевидно нельзя
    #
    # Создавать кортеж с длиной 0 – тоже нельзя, потому что () – специальный immortal объект, его создают в рамках старта интерпретатора один раз в pycore_runtime_init вот так: .tuple_empty = { .ob_base = _PyVarObject_HEAD_INIT(&PyTuple_Type, 0), }
    #
    # Если размер кортежа не очень большой (< 20), то еще пробуем использовать дополнительную оптимизацию с _Py_FREELIST_POP, о ней будет чуть позже
    #
    # Далее смотрим, что если размер кортежа очень большой – сразу кидаем ошибку памяти, чтоб не аллоцировать слишком много
    #
    # В самом конце используем PyObject_GC_NewVar для инициализации PyTupleObject, внутреннего PyVarObject и физического выделения памяти
    #
    # Вот как выглядит PyObject_GC_NewVar (кстати, прямо сейчас их два: для обычного билда и для nogil, но отличий вроде бы нет):
    #
    # PyVarObject *
    # _PyObject_GC_NewVar(PyTypeObject *tp, Py_ssize_t nitems)
    # {
    #     PyVarObject *op;
    #
    #     if (nitems < 0) {
    #         PyErr_BadInternalCall();
    #         return NULL;
    #     }
    #     size_t presize = _PyType_PreHeaderSize(tp);
    #     size_t size = _PyObject_VAR_SIZE(tp, nitems);
    #     op = (PyVarObject *)gc_alloc(tp, size, presize);
    #     if (op == NULL) {
    #         return NULL;
    #     }
    #     _PyObject_InitVar(op, tp, nitems);
    #     return op;
    # }
    # Тут есть два важных момента: gc_alloc для выделения памяти, про которую знает GC. И _PyObject_InitVar, который устанавливает ob_size и ob_base через Py_SET_SIZE и Py_SET_TYPE.
    #
    # Как GC выделяет память? Глубока же кроличья нора!
    #
    # static PyObject *
    # gc_alloc(PyTypeObject *tp, size_t basicsize, size_t presize)
    # {
    #     PyThreadState *tstate = _PyThreadState_GET();
    #     if (basicsize > PY_SSIZE_T_MAX - presize) {
    #         return _PyErr_NoMemory(tstate);
    #     }
    #     size_t size = presize + basicsize;
    #     // Смотри определение `_PyObject_MallocWithType` ниже:
    #     char *mem = _PyObject_MallocWithType(tp, size);
    #     if (mem == NULL) {
    #         return _PyErr_NoMemory(tstate);
    #     }
    #     ((PyObject **)mem)[0] = NULL;
    #     ((PyObject **)mem)[1] = NULL;
    #     PyObject *op = (PyObject *)(mem + presize);
    #     _PyObject_GC_Link(op);
    #     return op;
    # }
    #
    # // Sets the heap used for PyObject_Malloc(), PyObject_Realloc(), etc. calls in
    # // Py_GIL_DISABLED builds. We use different heaps depending on if the object
    # // supports GC and if it has a pre-header. We smuggle the choice of heap
    # // through the _mimalloc_thread_state. In the default build, this simply
    # // calls PyObject_Malloc().
    # static inline void *
    # _PyObject_MallocWithType(PyTypeObject *tp, size_t size)
    # {
    # #ifdef Py_GIL_DISABLED
    #     _PyThreadStateImpl *tstate = (_PyThreadStateImpl *)_PyThreadState_GET();
    #     struct _mimalloc_thread_state *m = &tstate->mimalloc;
    #     m->current_object_heap = _PyObject_GetAllocationHeap(tstate, tp);
    # #endif
    #     void *mem = PyObject_Malloc(size);
    # #ifdef Py_GIL_DISABLED
    #     m->current_object_heap = &m->heaps[_Py_MIMALLOC_HEAP_OBJECT];
    # #endif
    #     return mem;
    # }
    # Происходит много всего. Обращу внимание на несколько ключевых моментов:
    #
    # Выделение памяти всегда может завершиться ошибкой, что мы должны контролировать
    #
    # _PyObject_GC_Link добавляет объект в GC в молодое поколение объектов
    #
    # Выделение памяти в GIL и noGIL режимах – разное, про mimalloc в nogil можно почитать тут, в рамках данной статьи – перебор жести :)
    #
    # И вот уже внутри PyObject_Malloc мы физически выделим память для объекта в нужном размере
    #
    # Фух! Объект нужного размера мы создали. Обратите внимание, что нигде не было момента установки конкретных объектов в кортеж. Мы просто выделили память.
    #
    # А теперь давайте его скорее уничтожим! Чтобы иметь повод поговорить про деаллокацию.
    #
    # Смотрим на tp_dealloc, который срабатывает, перед вычищением объекта из памяти:
    #
    # Что происходит по шагам:
    #
    # Проверяем, что мы не деаллоцируем (), нужно для дебаг сборки
    #
    # Убираем текущий объект из GC с PyObject_GC_UnTrack
    #
    # Начинаем оптимизацию (и защиту стека) при удалении больших объектов с Py_TRASHCAN_BEGIN, о чем я писал подробно у себя в тг канале
    #
    # Проходимся по всем объектам в ob_item и нещадно декрефим их, чтобы уменьшить ob_refcnt и освободить их, если они больше нигде не используются
    #
    # А дальше – мы пытаемся сделать maybe_freelist_push, и если получилось, то мы не высвобождаем память и не вызываем tp_free. А освобождаем память, только когда не получилось запушить новый freelist. Тут настало время про них рассказать!
    #
    # Вообще, идея переиспользовать память нужного размера под объекты одинакового размера – совсем не нова. Тут ровно такое и происходит. При деаллокации мы для кортежей с размером <20 не высвобождаем память просто так. Мы понимаем, что кто-то скоро снова захочет создать кортеж такого размера. И нам не нужно будет выделять память (что долго), мы сможем просто переиспользовать существующие "ждущие" участки памяти.
    #
    # Следовательно – во время деаллокации мы складываем объекты кортежей нужного размера во freelist:
    #
    # static inline int
    # maybe_freelist_push(PyTupleObject *op)
    # {
    #     if (!Py_IS_TYPE(op, &PyTuple_Type)) {
    #         return 0;
    #     }
    #     Py_ssize_t index = Py_SIZE(op) - 1;
    #     if (index < PyTuple_MAXSAVESIZE) {
    #         return _Py_FREELIST_PUSH(tuples[index], op, Py_tuple_MAXFREELIST);
    #     }
    #     return 0;
    # }
    # А во время аллокации пробуем найти нужный нужного размера и переиспользовать. Помните, я обещал подробнее рассказать про _Py_FREELIST_POP? Теперь мы понимаем, зачем он нужен в tp_alloc:
    #
    # static PyTupleObject *
    # tuple_alloc(Py_ssize_t size)
    # {
    #     // ...
    #     Py_ssize_t index = size - 1;
    #     if (index < PyTuple_MAXSAVESIZE) {  // 20
    #         PyTupleObject *op = _Py_FREELIST_POP(PyTupleObject, tuples[index]);
    #         if (op != NULL) {
    #             return op;
    #         }
    #     }
    #     // ...
    # }
    # Если кортеж нужного размера есть в _Py_FREELIST, то мы просто возьмем его и вернем. Быстрее создание новых объектов. Быстрее сборка ненужных. Переиспользование памяти.
    #
    # Мы можем легко подтвердить мои слова следующим примером (специально берем большой размер, чтобы нигде внутри интерпретатора на создавались "утилитарные" кортежи, которые мы не увидим, малого размера):
    #
    # >>> a = tuple(range(18))
    # >>> id(a)
    # 4352063168
    # >>> del a
    #
    # >>> b = tuple(range(18))
    # >>> id(b)  # should be equal to `id(a)`
    # 4352063168
    # Смотрите! Адрес в памяти или id(b) такой же как id(a), который мы только что удалили. Теперь мы знаем, почему. Прикольная оптимизация?
    #
    # Мутабельность tuple
    # В заголовке было про мутабельность – где мутабельность? Обычно мы все привыкли смотреть на tuple как на иммутабельный объект; но в C-API все по-другому. Сейчас покажу. Создавать tuplы мы уже научились, но вот наполнять их объектами – еще нет. Давайте исправлять и наполнять!
    #
    # Во-первых, важно сказать: внешне из Python API – tuple не очень-то и мутабельный. Его можно (но не всегда нужно) мутировать только из C-API. Для C-API какой-то такой код будет абсолютно нормальным:
    #
    # PyObject *tup = PyTuple_New(2);
    # if (tup == NULL) {
    #     return NULL;
    # }
    #
    # PyTuple_SET_ITEM(tup, 0, first_obj);
    # PyTuple_SET_ITEM(tup, 1, second_obj);
    # Что мы тут видим? Мутацию tuple 😱
    #
    # Сначала мы устанавливаем 0 индекс и нужный объект, потом 1 индекс и нужный объект. Документация просит делать так только для новых кортежей, которые мы создаем внутри C кода. Но кто мы такие, чтобы читать документацию? 🌚️️
    #
    # Во-вторых, справедливости ради: PyTuple_SetItem чуть менее мутабельная функция, если можно так сказать. Потому что она проверяет, что у кортежа ob_refcnt равен 1. Что отсекает любые объекты, которые уже используются:
    #
    # int
    # PyTuple_SetItem(PyObject *op, Py_ssize_t i, PyObject *newitem)
    # {
    #     PyObject **p;
    #     if (!PyTuple_Check(op) || Py_REFCNT(op) != 1) {
    #         Py_XDECREF(newitem);
    #         PyErr_BadInternalCall();
    #         return -1;
    #     }
    #     if (i < 0 || i >= Py_SIZE(op)) {
    #         Py_XDECREF(newitem);
    #         PyErr_SetString(PyExc_IndexError,
    #                         "tuple assignment index out of range");
    #         return -1;
    #     }
    #     p = ((PyTupleObject *)op) -> ob_item + i;
    #     Py_XSETREF(*p, newitem);
    #     return 0;
    # }
    # В-третьих, есть нормальные АПИ для сбора tuple из существующих объектов: PyTuple_Pack и Py_BuildValue, про которые я рассказываю в лекции на видео.
    #
    # Ну и финально: команда разработки CPython задумывается сделать tuple иммутабельным и из C-API тоже. Но есть проблемы обратной совместимости. Старое АПИ уже множество лет используют разработчики примерно везде. Ссылка на обсуждение: https://github.com/python/cpython/issues/127058
    #
    # Похулиганим?
    # В качестве прикола я сделал свой модуль на C, который позволяет мутировать любые кортежи:
    #
    # >>> import mutable_tuple
    #
    # >>> x = (1, 2)
    # >>> mutable_tuple.set_item(x, 0, 5)
    #
    # >>> x
    # (5, 2)
    # Не используйте ни для чего серьезного. Но можно посмотреть исходники и чему-то научиться (например, так не делать).
    #
    # И самый финал: нам вообще не нужны никакие внешние зависимости, чтобы мутировать tuple в питоне. Смотрим на такой пример (пожалуйста, уберите от просмотра впечатлительных людей и детей):
    #
    # >>> tup1 = (1, 2)
    # >>> tup1_2 = tup1
    # >>> tup2 = (3, 4)
    #
    # >>> import ctypes
    # >>> offset = (
    # ...     ctypes.sizeof(ctypes.c_ssize_t)    # skip ob_refcnt
    # ...     + ctypes.sizeof(ctypes.c_void_p)   # skip ob_base
    # ...     + ctypes.sizeof(ctypes.c_ssize_t)  # skip ob_item
    # ... )
    # >>> size = ctypes.sizeof(ctypes.c_void_p) * len(tup1)
    # >>> ctypes.memmove(id(tup1) + offset, id(tup2) + offset, size)
    #
    # >>> tup1, tup1_2, tup2
    # ((3, 4), (3, 4), (3, 4))
    # Тут мы просто двигаем память из одного объекта в другой. Можно ли считать данный подход мутацией? Напишите в коментариях. Вопрос спорный. Но так 100% лучше не делать. "Или живите дальше в проклятом мире, который сами и создали".
    #
    # Шалость удалась! Больше мы такой код обещаем не писать!
    #
    # Заключение
    # Всем большое спасибо за интерес к деталям питона, прочитать такую статью было не просто! Вы крутые!

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Tuples_01_ ()
#endif

#endmodule
