#------------------------------------------
# Functions_20_ ():
#------------------------------------------
def Functions_20_ ():
    """Functions_20_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Functions_20_.__name__)
    print ('#-----------------------------')

    # Как вызывать функции Go из Python с помощью ctypes
    # 11.06.2024GO, Python
    # Как вызывать функции Go из Python с помощью ctypes
    # В этой статье поговорим о том, как можно запускать программу, написанную на Go из Python. Зачем? При работе на Python иногда имеет смысл реализовать отдельные функции на статичном, высокопроизводительном языке. Go может стать отличным выбором для этого, потому что он быстрый, простой и кроссплатформенный. Недавно в моем Python канале, мы обсуждали, как это сделать, в результате родилась эта статья.
    #
    # Для реализации всех шагов нам потребуется: Python, компилятор Go и GCC (MinGW для Windows). Примеры кода доступны в репо на Github.
    #
    # Стоит отметить, что существуют и другие способы вызова Go из Python — SWIG, например. Здесь же мы рассмотрим ctypes, потому что он не требует дополнительных зависимостей и очень прост.
    #
    # Поехали!
    #
    # Hello world
    # Начнем с hello-world, куда же без него
    #
    # hello.go
    #
    # package main
    #
    # import "C"
    # import "fmt"
    #
    # //export hello
    # func hello() {
    #     fmt.Println("Hello world!")
    # }
    #
    # func main() {}
    # Теперь собираем на основе hello.go файл hello.dll — для этого компилируем первый с флагом -buildmode=c-shared
    #
    # # Windows:
    # go build -o hello.dll -buildmode=c-shared hello.go
    # # Linux:
    # go build -o hello.so -buildmode=c-shared hello.go
    # Теперь, для использования hello.dll в Python нам нужно подключить этот файл, используя ctypes.CDLL():
    #
    # hello.py
    #
    # import ctypes
    #
    # lib = ctypes.CDLL('./hello.dll')  # Or hello.so if on Linux.
    # hello = lib.hello
    #
    # hello()
    # Запустим:
    #
    # > python hello.py
    # Hello world!
    # Отлично; тут стоит отметить пару моментов:
    #
    # Go-код абсолютно стандартный, единственное — нужно указать //export hello для экспортирования функции hello для внешнего использования
    # Сборка с флагом -buildmode=c-shared создает общую библиотеку в стиле C.
    # Загрузка такой библиотеки в Python реализуется через ctypes.CDLL()
    # Простой ввод и вывод
    # Что ж, теперь функция будет принимать некоторые аргументы и возвращать значение:
    #
    # primitive.go
    #
    # //export add
    # func add(a, b int64) int64 {
    #     return a + b
    # }
    # primitive.py
    #
    # lib = ctypes.CDLL('./primitive.dll')
    # add = lib.add
    #
    # # конвертируем значения в C-представление
    # add.argtypes = [ctypes.c_int64, ctypes.c_int64]add.restype = ctypes.c_int64
    #
    # print('10 + 15 =', add(10, 15))
    # Запускаем:
    #
    # > python add.py
    # 10 + 15 = 25
    # Итак, чтобы передать входные данные и получить выходные данные из функции Go, нужно использовать атрибуты argtypes и restype из библиотеки ctypes. Пару моментов:
    #
    # argtypes проверяет аргументы перед вызовом библиотечного кода
    # Использование этих атрибутов указывает Python, как преобразовать входные значения Python в значения ctypes, и как преобразовать выходные значения обратно в значения Python.
    # Кстати, можно поискать соответствие между типами C и типами Go в сгенерированном файле .h после компиляции вашего кода Go с -buildmode=c-shared.
    #
    # Attention: строго говоря, типы тесно связаны с архитектурой железа. В общем случае безопаснее использовать размерные типы (int64), чем безразмерные (int)
    #
    # Массивы и срезы
    # Окей, теперь поговорим о массивах и срезах. При этом мы вступаем в зону незащищенного доступа к памяти — хотя Python и Go в целом безопасны по памяти, работа с необработанными указателями может привести к переполнению буфера или утечкам.
    #
    # arrays.go
    #
    # // возвращает квадраты введённых чисел
    # //
    # //export squares
    # func squares(numsPtr *float64, outPtr *float64, n int64) {
    #     nums := unsafe.Slice(numsPtr, n)
    #     out := unsafe.Slice(outPtr, n)
    #
    #     // кстати, для Go < 1.17
    #     // nums := (*[1 << 30]float64)(unsafe.Pointer(numsPtr))[:n:n]   // out := (*[1 << 30]float64)(unsafe.Pointer(outPtr))[:n:n]
    #     for i, x := range nums {
    #         out[i] = x * x
    #     }
    # }
    # arrays.py
    #
    # И вызываем эту dll в Python:
    #
    # lib = ctypes.CDLL('./arrays.dll')
    # squares = lib.squares
    #
    # squares.argtypes = [
    #     ctypes.POINTER(ctypes.c_double),
    #     ctypes.POINTER(ctypes.c_double),
    #     ctypes.c_int64,
    # ]
    # # использовать from_buffer() более эффективно, чем просто делать:
    # # (ctypes.c_double * 3)(*[1, 2, 3])
    # nums = array('d', [1, 2, 3])
    # nums_ptr = (ctypes.c_double * len(nums)).from_buffer(nums)
    # out = array('d', [0, 0, 0])
    # out_ptr = (ctypes.c_double * len(out)).from_buffer(out)
    #
    # squares(nums_ptr, out_ptr, len(nums))
    # print('nums:', list(nums))
    # print('out:', list(out))
    # Запускаем:
    #
    # > python squares.py
    # nums: [1.0, 2.0, 3.0]out: [1.0, 4.0, 9.0]
    # Итоги: для работы со списками нам необходимо преобразовать их в массивы C. Для этого нужно создать массив с помощью (ctypes.my_type * my_length)(1, 2, 3 ...). Более быстрый способ — использовать библиотеку array, как показано выше. Ещё коснёмся этого чуть позже, когда будем говорить о бенчмарках.
    #
    # В Go можно сделать, чтобы C-подобный указатель указывал на срез. Таким образом, можно использовать синтаксис Go при работе с буферами Python.
    #
    # Ещё пара моментов: нельзя вернуть указатель Go при использовании CGo, это приведет к ошибке. Вместо этого можно выделить указатель на C из Go с помощью C.malloc() и вернуть его. Однако при этом сборщик мусора никак не взаимодействует с такими указателями, поэтому нужно предусмотреть механизм удаления таких указателей, чтобы не получить утечку памяти.
    #
    # Что тут можно рекомендовать? Чтобы функция могла безопасно возвращать массив из Go нужно либо предварительно аллоцировать для них память в Python и передавать в Go в качестве аргументов, либо генерировать массивы в Go и оборачивать их в безопасную структуру (чуть коснёмся этого дальше).
    #
    # Подведём краткое описание опасностей:
    #
    # Возврат указателей Go в Python. Ошибка.
    # Возврат указателей C из Go в Python без явного удаления. Утечка памяти.
    # Потеря ссылки ctypes во время выполнения кода Go (например, при получении ctypes.addressof и сбросе объекта-указателя). Возможная ошибка сегментации.
    # Строки
    # Строки устроены практически как массивы в плане управления памятью, поэтому все, что связано с массивами, применимо и к ним. Давайте обсудим пару полезных приёмов и некоторые подводные камни:
    #
    # string.go
    #
    # //export repeat
    # func repeat(s *C.char, n int64, out *byte, outN int64) *byte {
    #     // помещаем наш выходной буфер в буфер Go
    #     outBytes := unsafe.Slice(out, outN)[:0] buf := bytes.NewBuffer(outBytes)
    #
    #     var goString string = C.GoString(s) // копируем ввод в пространство памяти Go
    #     for i := int64(0); i < n; i++ {
    #         buf.WriteString(goString)
    #     }
    #     buf.WriteByte(0) // важно - нулевой байт в конец строки
    #     return out
    # }
    # string.py
    #
    # lib = ctypes.CDLL('./string.dll')
    # repeat = lib.repeat
    #
    # repeat.argtypes = [
    #     ctypes.c_char_p,
    #     ctypes.c_int64,
    #     ctypes.c_char_p,
    #     ctypes.c_int64,
    # ]repeat.restype = ctypes.c_char_p
    #
    # #
    # buf_size = 1000
    # buf = ctypes.create_string_buffer(buf_size)
    #
    # result = repeat(b'Badger', 4, buf, buf_size)  # type(result) = bytes
    # print('Badger * 4 =', result.decode())
    #
    # result = repeat(b'Snake', 5, buf, buf_size)
    # print('Snake * 5 =', result.decode())
    # Запускаем:
    #
    # > python repeat.py
    # Badger * 4 = BadgerBadgerBadgerBadger
    # Snake * 5 = SnakeSnakeSnakeSnakeSnake
    # Строки передаются путем преобразования строки Python в объект bytes (обычно с помощью вызова encode()), затем в C-указатель и затем в Go-строку.
    #
    # Использование ctypes.c_char_p в argtypes заставляет Python ожидать объект bytes и преобразовывать его в C *char. В restype он преобразует возвращаемый *char в объект bytes.
    #
    # В Go вы можете преобразовать *char в строку Go с помощью C.GoString. Это копирует данные и создает новую строку, управляемую Go с точки зрения сборки мусора. Чтобы создать *char в качестве возвращаемого значения, можно вызвать C.CString. Однако указатель будет потерян, если вы не сохраните на него ссылку, и тогда произойдет утечка памяти. Чтобы вернуть строки из Go, можно использовать те же приемы, что и при работе с массивами.
    #
    # Если указатель на вывод был передан Python, Go может вернуть его, и Python автоматически создаст из него объект bytes.
    #
    # Итак, какие проблемы могут возникнуть?
    #
    # Возвращение C.CString без сохранения ссылки для последующего удаления. Утечка памяти.
    # Не добавление нулевого байта в конец выводимой строки. Переполнение буфера при преобразовании в объект Python.
    # Отсутствие проверки размера выходного буфера в Go. Переполнение буфера или неполный вывод.
    # Массив строк
    # Кстати, передать массив строк можно так:
    #
    # join.go
    #
    # func goStrings(cstrs **C.char) []string {
    #     var result []string
    #     slice := unsafe.Slice(cstrs, 1<<30)
    #     for i := 0; slice[i] != nil; i++ {
    #         result = append(result, C.GoString(slice[i]))
    #     }
    #     return result
    # }
    # join.py
    #
    # def to_c_str_array(strs: List[str]):
    #     ptr = (ctypes.c_char_p * (len(strs) + 1))()
    #     ptr[:-1] = [s.encode() for s in strs]    ptr[-1] = None
    #     return ptr
    # Numpy и Pandas
    # Доступ к буферам NumPy предоставляется с помощью синтаксиса .ctypes.data_as(ctypes.whatever). В pandas можно использовать атрибут .values для получения базового массива NumPy, а затем использовать синтаксис NumPy для получения фактического указателя. Таким образом, можно изменять массив/таблицу на месте, выглядит наподобие:
    #
    # numpypandas.go
    #
    # //export increase
    # func increase(numsPtr *int64, n int64, a int64) {
    #     nums := unsafe.Slice(numsPtr, n)
    #     for i := range nums {
    #         nums[i] += a
    #     }
    # }
    # numpypandas.py
    #
    # lib = ctypes.CDLL('./numpypandas.dll')
    # increase = lib.increase
    #
    # increase.argtypes = [
    #     ctypes.POINTER(ctypes.c_int64),
    #     ctypes.c_int64,
    #     ctypes.c_int64,
    # ]
    # people = pandas.DataFrame({
    #     'name': ['Alice', 'Bob', 'Charlie'],
    #     'age': [20, 30, 40],
    # })
    #
    # # проверяем тип
    # ages = people.age
    # if str(ages.dtypes) != 'int64':
    #     raise TypeError(f'Expected type int64, got {ages.dtypes}')
    #
    # values = ages.values  # type=numpy.Array
    # ptr = values.ctypes.data_as(ctypes.POINTER(ctypes.c_int64))
    #
    # print('Before')
    # print(people)
    #
    # print('After')
    # increase(ptr, len(people), 5)
    # print(people)
    # Запускаем:
    #
    # > python table.py
    # Before
    #       name  age
    # 0    Alice   20
    # 1      Bob   30
    # 2  Charlie   40
    # After
    #       name  age
    # 0    Alice   25
    # 1      Bob   35
    # 2  Charlie   45
    # >
    # Важно проверить тип массива, прежде чем передавать его в функцию Go, ведь данные могут быть другого числового типа (int<->float), другого размера (int64<->int32) или типа вообще object.
    #
    # Еще один момент, о котором следует помнить, — Pandas копирует таблицы при выборе строк. Скажем, если у нас есть DataFrame с именем people, то people[people['age'] < 40]вернет копию people. Поэтому передача копии в Go не повлияет на исходную таблицу.
    #
    # Структуры
    # Чтобы работать со структурами, необходимо определить их как в Python, так и в C. Экспорт структур Go невозможен.
    #
    # structs.go
    #
    # /*
    # struct person {
    #   char* firstName;
    #   char* lastName;
    #   char* fullName;
    #   long long fullNameLen;
    # };
    # */
    # import "C"
    # import (
    #     "bytes"
    #     "unsafe"
    # )
    #
    # //export fill
    # func fill(p *C.struct_person) {
    #     buf := bytes.NewBuffer(unsafe.Slice((*byte)(unsafe.Pointer(p.fullName)),
    #         p.fullNameLen)[:0])
    #     first := C.GoString(p.firstName)
    #     last := C.GoString(p.lastName)
    #     buf.WriteString(first + " " + last)
    #     buf.WriteByte(0)
    # }
    # structs.py
    #
    # class Person(ctypes.Structure):
    #     _fields_ = [
    #         ('first_name', ctypes.c_char_p),
    #         ('last_name', ctypes.c_char_p),
    #         ('full_name', ctypes.c_char_p),
    #         ('full_name_len', ctypes.c_int64),
    #     ]
    #
    # lib = ctypes.CDLL('./structs.dll')
    #
    # fill = lib.fill
    # fill.argtypes = [ctypes.POINTER(Person)]
    # buf_size = 1000
    # buf = ctypes.create_string_buffer(buf_size)
    # person = Person(b'John', b'Galt', buf.value, len(buf))
    # fill(ctypes.pointer(person))
    #
    # print(person.full_name)
    # Поскольку мы не можем экспортировать структуры Go, мы определяем их на языке C, добавляя комментарий над строкой import "C". Кстати, как видно, в Go структура personобозначается как C.struct_person. В Python мы определяем эквивалентный класс ctypes.Structure, который имеет точно такие же поля.
    #
    # Можно заполнять поля struct в Go, используя простые примитивы. Если же используются массивы и строки, действуют те же ограничения, что и раньше.
    #
    # Автоматическое управление памятью при помощи __del__
    # Настройка удобной и безопасной схемы управления памятью — последнее, что осталось сделать, приступим. Используя дандер-метод Python (__del__), мы можем удобно аллоцировать память под буферы в Go (C), и освобождать её в Python, когда объект удаляется.
    #
    # Эта схема проста и требует 2 вещей: функции в Go, которая будет деаллоцировать память для объекта, и функции в Python, который будет вызывать функцию Go.
    #
    # Функция Python будет вызвана автоматически, когда количество ссылок на объект станет равным нулю.
    #
    # del.go
    #
    # /*
    # #include <stdlib.h>
    # struct userInfo {
    #   char* info;
    # };
    # */
    # import "C"
    # import (
    #     "fmt"
    #     "unsafe"
    # )
    #
    # // аллоцируем память для объекта
    # //
    # //export getUserInfo
    # func getUserInfo(cname *C.char) C.struct_userInfo {
    #     var result C.struct_userInfo
    #     name := C.GoString(cname)
    #     result.info = C.CString(
    #         fmt.Sprintf("User %q has %v letters in their name",
    #             name, len(name)))
    #     return result
    # }
    #
    # // деаллоцируем память для объекта
    # //
    # //export delUserInfo
    # func delUserInfo(info C.struct_userInfo) {
    #     // печатаем для наглядности
    #     fmt.Printf("Freeing user info: %s\n", C.GoString(info.info))
    #     C.free(unsafe.Pointer(info.info))
    # }
    # del.py
    #
    # class UserInfo(ctypes.Structure):
    #     _fields_ = [('info', ctypes.c_char_p)]
    #     def __del__(self):
    #         del_user_info(self)
    #
    # lib = ctypes.CDLL('del.dll')
    # get_user_info = lib.getUserInfo
    # get_user_info.argtypes = [ctypes.c_char_p]get_user_info.restype = UserInfo
    # del_user_info = lib.delUserInfo
    # del_user_info.argtypes = [UserInfo]
    # def work_work():
    #     user1 = get_user_info('Alice'.encode())
    #     print('Info:', user1.info.decode())
    #     print('-----------')
    #
    #     user2 = get_user_info('Bob'.encode())
    #     print('Info:', user2.info.decode())
    #     print('-----------')
    #
    #     # В этот момент объекты user1 и user2 должны быть удалены
    #
    # work_work()
    # print('Did I remember to free my memory?')
    # Запускаем:
    #
    # Name: Alice
    # Description: User "Alice" has 5 letters in their name
    # Name length: 5
    # -----------
    # Name: Bob
    # Description: User "Bob" has 3 letters in their name
    # Name length: 3
    # -----------
    # Freeing user info: User "Alice" has 5 letters in their name
    # Freeing user info: User "Bob" has 3 letters in their name
    # Did I remember to free my memory?
    # Великолепно
    #
    # Обработка ошибок
    # Передача ошибок Go обратно в Python необходима для полноценной работы программы. Для этого мы создадим многократно используемый тип ошибки.
    #
    # error.go
    #
    # /*
    # #include <stdlib.h>
    # typedef struct {
    #     char* err;
    # } error;
    # */
    # import "C"
    #
    # // ...
    #
    # func newError(s string, args ...interface{}) C.error {
    #     if s == "" {
    #         return C.error{}  // эквивалентно ошибке nil в Go
    #     }
    #     msg := fmt.Sprintf(s, args...)
    #     return C.error{C.CString(msg)}
    # }
    #
    # //export delError
    # func delError(err C.error) {
    #     if err.err == nil {
    #         return
    #     }
    #     C.free(unsafe.Pointer(err.err))
    # }
    # error.py
    #
    # class Error(ctypes.Structure):
    #     _fields_ = [('err', ctypes.c_char_p)]
    #     def __del__(self):
    #         if self.err is not None:
    #             del_error(self)
    #
    #     def raise_if_err(self):
    #         if self.err is not None:
    #             raise IOError(self.err.decode())
    #
    # # ...
    #
    # del_error = lib.delError
    # del_error.argtypes = [Error]
    # Отлично, теперь мы можем использовать новый тип Error в структурах и функциях с несколькими возвращаемыми значениями
    #
    # Немного о повышении производительности
    # Стоимость пустого вызова
    # Стоимость пустого вызова функции — в районе 5 мкс. Немало, по сравнению с вызовом нативной функции. Получается, что CGo имеет высокие накладные расходы на вызов. Причём это происходит и при вызове Go из нативного кода на Си, независимо от того, связан ли код Go через динамическую или статическую библиотеку.
    #
    # Эти накладные расходы следует учитывать при проектировании API. Если на каждый вызов функции приходится 5 мкс работы Go, то на накладные расходы на вызов будет тратиться 50% времени. Если на каждый вызов функции приходится 500 операций Go, то накладные расходы на вызовы составят около 1%.
    #
    # Переиспользование памяти
    # Для вызовов, которые повторяются много раз, если это имеет смысл можно аллоцировать память 1 раз с помощью ctypes и использовать её повторно для всех повторяющихся вызовов.
    #
    # Выглядит это наподобие:
    #
    # # обёртка ctypes для функции в Go
    # my_function = my_lib.my_function
    #
    # def my_function_with_buffer(n: int):
    #     buffer = (ctypes.c_char * n)(*([0] * n))
    #     def my_function_with_closure():
    #         my_function(buffer, n)
    #     return my_function_with_closure
    #
    # def work_work():
    #     my_function_buffered = my_function_with_buffer(1000)
    #     my_function_buffered()
    #     my_function_buffered()
    #     my_function_buffered()
    # Использование библиотеки array для аллокации памяти
    # Как уже упоминалось выше, использование библиотеки array для аллокации памяти быстрее, чем обычный конструктор значения (ctypes.type * n).
    #
    # Бенчмарки
    # Ну и напоследок несколько сравнений, иллюстрирующих преимущество от вызова функций Go из Python по сравнению с использованием просто функций Python. Для полноты картины все измерения включают накладные расходы на преобразование значений в C-представление и обратно.
    #
    # Вычисление π
    # Простое вычисление числа π, чтобы получить представление о том, насколько быстрее может быть Go.
    #
    # pi
    # pi
    # Перемешивание 10M элементов в случайном порядке
    # Хмм, получается использование Go может быть быстрее даже встроенных модулей Python.
    #
    # shuffle
    # shuffle
    # Использование array и метод, рекомендованный ctypes
    # Сравнение метода, рекомендованного ctypes, с использованием array для преобразования значений Python в значения C.
    #
    # # используем ctypes
    # cvals = (ctypes.c_double * n)(*nums)
    #
    # # используем array
    # arr = array('d', nums)
    # cvals = (ctypes.c_double * n).from_buffer(arr)
    # list
    # list
    # Что ж, вот мы и обсудили, как можно вызывать Go из Python, спасибо Гвидо за возможность использовать сишные библиотеки в Python
    #
    # Если были какие-то неточности — поправьте в комментах
    #
    # Кстати, я веду телеграм-канал по Python, в котором описываю интересные фреймворки, библиотеки, open-source инструменты и не только
    # , а тем, кто любит и изучает Golang, могу посоветовать другой отличный ресурс. Вероятно, там вы сможете найти что-то полезное для себя, так что welcome)
    #
    # Большое спасибо за прочтение этой статьи!

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Functions_20_ ()
#endif

#endmodule
