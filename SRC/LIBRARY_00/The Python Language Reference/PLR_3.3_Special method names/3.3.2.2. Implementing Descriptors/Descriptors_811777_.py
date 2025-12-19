#------------------------------------------
# Descriptors_811777 ():
#------------------------------------------
def Descriptors_811777 ():
    """Descriptors_811777"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Descriptors_811777.__name__)
    print ('#-----------------------------')

    # Python — Дескрипторы (Descriptors)
    # https://habr.com/ru/articles/811777/
    # Python — Дескрипторы (Descriptors)
    # Средний
    # 8 мин
    # 16K
    # Python
    # *
    # Если обратиться к документации, то дескриптор — механизм, который позволяет объектам настраивать поиск, хранение и удаление атрибутов.
    #
    # Дескрипторы используются в классах, выступая в роли атрибутов класса(не экземпляра).
    #
    # Думаю, мало кто, хотя бы раз, сам писал дескрипторы в коммерческой разработке, но я уверен, что большинство программистов используют механизмы, которые являются дескрипторами, или используют их "под капотом":
    #
    # classmethod, staticmethod
    #
    # property
    #
    # __slots__
    #
    # В конечном итоге, любое обращение к атрибуту класса, связано с дескрипторами.
    #
    # Некоторые из них, мы реализуем с вами немного позднее.
    #
    # Протокол дескрипторов состоит из:
    #
    # __get__ - Поиск атрибута
    #
    # __set__ - Хранение атрибута
    #
    # __delete__ - Удаление атрибута
    #
    # Начнём с поиска атрибута - __get__ .
    #
    # class StaticValueDescriptor:
    #     def __init__(self, value: Any) -> None:
    #         self._value = value
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return self._value
    #
    #
    # class Object:
    #     attr_1 = StaticValueDescriptor(100)
    #
    #
    # instance_object = Object()
    # instance_object.attr_1  # -> 100
    # Несмотря на то, что в attr_1 мы присвоили экземпляр StaticValueDescriptor, в ответе мы видим 100, но почему?
    #
    # Дело в том, что при поиске атрибута класса(getattribute), python использует примерно такой механизм(подчеркнул одинаковые куски алгоритма):
    #
    # attr_1 есть в __dict__ класса?
    #
    # Да. Есть ли у него __get__ и (__set__ или __delete__)(data descriptor)?
    #
    # Да. Для получения результата используется дескриптор.
    #
    # Нет. attr_1 есть в __dict__ экземпляра?
    #
    # Да. Вернуть результат из __dict__ экземпляра.
    #
    # Нет. attr_1 есть в __dict__ класса?
    #
    # Да. Есть ли у него __get__ (non-data descriptor)?
    #
    # Да. Для получения результата используется дескриптор.
    #
    # Нет. Вернуть результат из __dict__ класса.
    #
    # Нет. Вызов у класса getattr , который по умолчанию возбудит исключение AttributeError.
    #
    # Нет. attr_1 есть в __dict__ экземпляра?
    #
    # Да. Вернуть результат из __dict__ экземпляра.
    #
    # Нет. attr_1 есть в __dict__ класса?
    #
    # Да. Есть ли у него __get__ (non-data descriptor)?
    #
    # Да. Для получения результата используется дескриптор.
    #
    # Нет. Вернуть результат из __dict__ класса.
    #
    # Нет. Вызов у класса getattr , который по умолчанию возбудит исключение AttributeError.
    #
    # Согласен, некоторым, такое представление алгоритма покажется сложным. Я упрощу его и покажу лишь приоритеты получения атрибута при поиске:
    #
    # Data descriptor - дескриптор, у которого есть __get__ и (__set__ или __delete__)
    #
    # Instance.__dict__
    #
    # Следующие два варианта имеют одинаковый приоритет.
    #
    # Non-data descriptor - дескриптор, у которого есть только __get__
    #
    # Class.__dict__
    #
    # Мы ещё вернёмся к примерам, которые продемонстрируют работу приоритетов на деле, а пока давайте вернёмся к протоколу дескрипторов.
    #
    # Ещё не дойдя до __set__ или __delete__ у вас, может возникнуть вопрос - "а как связать конкретный дескриптор с конкретным атрибутом? Я не хочу использовать только хардкодные статические объекты". И правда, предыдущий пример со StaticValueDescriptor имеет достаточно узкую применимость.
    #
    # Решением с ходу является расширение __init__. И давайте сразу реализуем __set__:
    #
    # class DataDescriptor:
    #     def __init__(self, attr_name: str) -> None:
    #         self._attr_name = attr_name
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return instance.__dict__[self._attr_name]
    #
    #     def __set__(self, instance, value: Any) -> None:
    #         instance.__dict__[self._attr_name] = value
    #
    #
    # class Object:
    #   attr_1 = DataDescriptor("attr_1")
    #
    #
    # instance_object = Object()
    # instance_object.attr_1 = 100
    # instance_object.attr_1  # -> 100
    # В целом мы решили проблему, и смогли связать имя атрибута в рамках класса, где используется дескриптор, но можно сделать ещё лучше, используя __set_name__:
    #
    # class DataDescriptor:
    #     def __set_name__(self, owner, attr_name: str) -> None:
    #         self._attr_name = attr_name
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return instance.__dict__[self._attr_name]
    #
    #     def __set__(self, instance, value: Any) -> None:
    #         instance.__dict__[self._attr_name] = value
    #
    #
    # class Object:
    #     attr_1 = DataDescriptor()
    #
    #
    # instance_object = Object()
    # instance_object.attr_1 = 100
    # instance_object.attr_1  # -> 100
    # Используя метод __set_name__ нам не нужно пробрасывать название переменной снаружи. Хотя уверен, найдутся те, кому нужно это:
    #
    # class DataDescriptor:
    #     def __init__(self, attr_name: str) -> None:
    #         self._attr_name = attr_name
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return instance.__dict__[self._attr_name]
    #
    #     def __set__(self, instance, value: Any) -> None:
    #         instance.__dict__[self._attr_name] = value
    #
    #
    # class Object:
    #     attr_1 = DataDescriptor("attr_999")  # Не надо так 😊
    #
    #     def __init__(self):
    #         self.attr_1 = 123
    #
    #
    # instance_object = Object()
    # instance_object.attr_999  # -> 123
    # Ну и напоследок у нас остаётся __delete__ :
    #
    # class DataDescriptor:
    #     def __set_name__(self, owner, attr_name: str) -> None:
    #         self._attr_name = attr_name
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return instance.__dict__[self._attr_name]
    #
    #     def __set__(self, instance, value: Any) -> None:
    #         instance.__dict__[self._attr_name] = value
    #
    #     def __delete__(self, instance) -> None:
    #         del instance.__dict__[self._attr_name]
    #
    #
    # class Object:
    #     attr_1 = DataDescriptor()
    #
    #
    # instance_object = Object()
    # instance_object.attr_1 = 100
    # instance_object.attr_1  # -> 100
    # del instance_object.attr_1
    # instance_object.attr_1  # -> KeyError: 'attr_1'
    # Ничего не смущает? А что это за KeyError при получении атрибута класса? Непорядок!
    #
    # Дело в том, что при вызове __get__ , наша попытка достать результат из instance.__dict__ терпит неудачу, так как такого ключа в словаре нет.
    #
    # Получается, нам нужно обработать исключение KeyError в __get__ , __set__ , __delete__ и следовать алгоритму, описанному выше. Кажется, не очень удобным делать это руками, неправда ли? Выход есть!
    #
    # Первый шаг - использовать встроенные механизмы(getattr, setattr, delattr), которые дадут нам корректное поведение:
    #
    # class DataDescriptor:
    #     def __set_name__(self, owner, attr_name: str) -> None:
    #         self._attr_name = attr_name
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return getattr(instance, self._attr_name)
    #
    #     def __set__(self, instance, value: Any) -> None:
    #         setattr(instance, self._attr_name, value)
    #
    #     def __delete__(self, instance) -> None:
    #         delattr(instance, self._attr_name)
    #
    #
    # class Object:
    #     attr_1 = DataDescriptor()
    #
    #
    # instance_object = Object()
    # instance_object.attr_1 = 100
    # instance_object.attr_1  # -> 100
    # del instance_object.attr_1
    # instance_object.attr_1  # -> RecursionError: maximum recursion depth
    #                         # exceeded while calling a Python object
    # Кажется, у нас проблемы? При попытке доступа к attr_1 происходит следующее:
    #
    # Мы всё по тому же алгоритму выбираем источником данных дескриптор и попадаем в __get__ .
    #
    # Внутри мы используем getattr(instance, self._attr_name, value)
    #
    # Который, в свою очередь пытается получить из экземпляра класса атрибут attr_1(по сути, то же самое, что мы пытались сделать изначально)
    #
    # И мы снова попадаем в дескриптор и так по кругу.
    #
    # И на эту проблему есть решение!
    #
    # Второй шаг - добавить защищённый(protected) вариант имени атрибута:
    #
    # class DataDescriptor:
    #     def __set_name__(self, owner, attr_name: str) -> None:
    #         self._protected_attr_name = f"_{attr_name}"
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return getattr(instance, self._protected_attr_name)
    #
    #     def __set__(self, instance, value: Any) -> None:
    #         setattr(instance, self._protected_attr_name, value)
    #
    #     def __delete__(self, instance) -> None:
    #         delattr(instance, self._protected_attr_name)
    #
    #
    # class Object:
    #     attr_1 = DataDescriptor()
    #
    #
    # instance_object = Object()
    # instance_object.attr_1 = 100
    # instance_object.attr_1  # -> 100
    # del instance_object.attr_1
    # instance_object.attr_1  # -> AttributeError: 'Object' object has no attribute
    #                         # '_attr_1'. Did you mean: 'attr_1'?
    # Теперь мы добились корректной ошибки!
    #
    # Возможно, некоторые из вас зададутся вопросом - "Куда делась проблема с рекурсией? Кажется, что в коде нет существенных изменений."
    #
    # Давайте разберём, что изменилось при обращении к attr_1:
    #
    # Мы всё по тому же алгоритму выбираем источником данных дескриптор и попадаем в __get__ .
    #
    # Внутри мы используем getattr(instance, self._attr_name, value)
    #
    # Который пытается получить из экземпляра класса не attr_1, а _attr_1. _attr_1 не является дескриптором и поэтому не повлечёт за собой повторный вызов __get__ и зацикливание, приводящее к ошибке(RecursionError)
    #
    # Таким образом, в экземпляре класса будет установлен атрибут _attr_1 , который не является дескриптором:
    #
    # instance_object = Object()
    # instance_object.__dict__  # -> {}
    # instance_object.attr_1 = 100
    # instance_object.__dict__  # -> {"_attr_1": 100}
    # И напоследок, давайте разберём разницу между data и non-data дескрипторами. Она заключается в приоритетах поиска атрибута.
    #
    # Data descriptor имеет __get__ и (__set__ или __delete__):
    #
    # class StaticValueDescriptor:
    #     def __init__(self, value: Any) -> None:
    #         self._value = value
    #
    #     def __set_name__(self, owner, attr_name: str) -> None:
    #         self._protected_attr_name = f"_{attr_name}"
    #
    #     def __get__(self, instance, owner=None) -> None:
    #         return self._value
    #
    #     def __set__(self, instance, value: Any) -> None:
    #         setattr(instance, self._protected_attr_name, value)
    #
    #
    # class Object:
    #     attr_1 = StaticValueDescriptor(100)
    #
    #     def __init__(self):
    #         self.attr_1 = 200
    #
    #
    # object_ = Object()
    # object_.attr_1  # -> 100 - data descriptor имеет приоритет
    #                 # над __dict__ экземпляра класса
    # Стоит нам закомментировать/удалить метод __set__, и мы получим non-data descriptor, у которого меньший приоритет, чем у __dict__ класса.
    #
    # class StaticValueDescriptor:
    #     ...
    #
    #     # def __set__(self, instance, value: Any) -> None:
    #     #    setattr(instance, self._private_attr_name, value)
    #
    #
    # class Object:
    #     attr_1 = StaticValueDescriptor(100)
    #
    #     def __init__(self):
    #         self.attr_1 = 200
    #
    #
    # object_ = Object()
    # object_.attr_1  # -> 200
    # После того, как мы получили описание работы дескрипторов, предлагаю вернуться к началу статьи и обсудить механизмы, которые так или иначе связаны с дескрипторами. Я покажу одну из возможных реализаций этих механизмов на python.
    #
    # staticmethod - Это non-data descriptor с одной задачей - просто вернуть тот же метод, что и был получен. Таким образом, мы избавляемся от self.
    #
    # Ваша idea может указывать на ошибку, но на самом деле всё будет работать.
    # Ваша idea может указывать на ошибку, но на самом деле всё будет работать.
    # class StaticMethod:
    #     def __init__(self, method: Callable) -> None:
    #         self._method = method
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return self._method
    #
    #
    # class Object:
    #     @StaticMethod
    #     def attr_1():
    #         return 100
    #
    #
    # object_ = Object()
    # object_.attr_1()  # -> 100
    # classmethod - Не что иное, как non-data descriptor, который создаёт обёртку над изначальным методом, и вместо экземпляра класса(self), передаёт первым аргументом класс(cls).
    #
    # class ClassMethod:
    #     def __init__(self, method: Callable) -> None:
    #         self._method = method
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         @wraps(self._method)
    #         def wrapper(*args, **kwargs):
    #             return self._method(owner, *args, **kwargs)
    #         return wrapper
    #
    #
    # class Object:
    #     @ClassMethod
    #     def attr_1(cls):
    #         return cls
    #
    #
    # object_ = Object()
    # object_.attr_1()  # -> <class 'main.Object'>
    # property - В угоду пониманию, я написал упрощённый вариант, который не во всех ситуациях будет работать так же, как бы работал привычный нам property. Однако при базовом использовании, он делает именно то, что от него ожидается:
    #
    # class Property:
    #     def __init__(
    #         self,
    #         fget: Callable | None = None,
    #         fset: Callable | None = None,
    #         fdel: Callable | None = None,
    #     ) -> None:
    #         self._fget = fget
    #         self._fset = fset
    #         self._fdel = fdel
    #
    #     def getattr(self, fget: Callable) -> Property:
    #         return type(self)(fget, self._fset, self._fdel)
    #
    #     def setattr(self, fset: Callable) -> Property:
    #         return type(self)(self._fget, fset, self._fdel)
    #
    #     def deleter(self, fdel: Callable) -> Property:
    #         return type(self)(self._fget, self._fset, fdel)
    #
    #     def __get__(self, instance, owner=None) -> Any:
    #         return self._fget(instance)
    #
    #     def __set__(self, instance, value) -> None:
    #         self._fset(instance, value)
    #
    #     def __delete__(self, instance) -> None:
    #         self._fdel(instance)
    #
    #
    # class Object:
    #     def __init__(self, value: Any) -> None:
    #         self._attr_1 = value
    #
    #     @Property
    #     def attr_1(self):
    #         return self._attr_1
    #
    #     @attr_1.setattr
    #     def attr_1(self, value: Any) -> None:
    #         self._attr_1 = value
    #
    #     @attr_1.deleter
    #     def attr_1(self) -> None:
    #         self._attr_1 = None
    #
    #
    # object_ = Object(100)
    # object_.attr_1  # -> 100
    # object_.attr_1 = 200
    # object_.attr_1  # -> 200
    # del object_.attr_1
    # object_.attr_1  # -> None
    # И в завершение без возможной реализации, хочется показать, что __slots__ тоже относится к дескрипторам:
    #
    # class Object:
    #     __slots__ = ("attr_1", "attr_2")
    #
    #
    # type(Object.attr_1)  # -> <class 'member_descriptor'>
    # type(Object.attr_2)  # -> <class 'member_descriptor'>
    # Спасибо всем, кто справился и дочитал статью до конца! Это была вводная статья о дескрипторах. Возможно, в будущем я напишу вторую часть, и покажу какие ещё вещи можно реализовывать с помощью этого протокола.


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Descriptors_811777 ()
#endif

#endmodule
