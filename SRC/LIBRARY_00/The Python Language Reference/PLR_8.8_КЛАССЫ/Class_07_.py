#------------------------------------------
# Class_07_ ():
#------------------------------------------
def Class_07_ ():
    """Class_07_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Class_07_.__name__)
    print ('#-----------------------------')

    # https://t.me/python_easy_ru/1046
    # 🤔 Какие есть методы у классов ?
    #
    # Классы могут содержать различные виды методов, которые
    # определяют поведение объектов и взаимодействие с ними.
    #
    # 🟠Обычные методы (Instance Methods)
    # Работают с экземплярами класса и могут изменять состояние
    # объекта. Они принимают как первый аргумент self, который
    # ссылается на экземпляр класса.
    # class MyClass:
    #     def __init__(self, value):
    #         self.value = value
    #
    #     def increment(self):
    #         self.value += 1
    #
    # # Использование
    # obj = MyClass(10)
    # obj.increment()
    # print(obj.value)  # Вывод: 11
    #
    # 🟠Методы класса (Class Methods)
    # Работают с самим классом, а не с экземплярами. Они принимают
    # как первый аргумент cls, который ссылается на класс. Методы
    # класса обозначаются декоратором @classmethod.
    # class MyClass:
    #     count = 0
    #
    #     def __init__(self):
    #         MyClass.count += 1
    #
    #     @classmethod
    #     def get_count(cls):
    #         return cls.count
    #
    # # Использование
    # obj1 = MyClass()
    # obj2 = MyClass()
    # print(MyClass.get_count())  # Вывод: 2
    #
    #
    # 🟠Статические методы (Static Methods)
    # Не зависят ни от экземпляра класса, ни от самого класса. Они
    # не принимают self или cls в качестве первого аргумента.
    # Статические методы обозначаются декоратором @staticmethod.
    # class MyClass:
    #     @staticmethod
    #     def greet(name):
    #         return f"Hello, {name}!"
    #
    # # Использование
    # print(MyClass.greet("Alice"))  # Вывод: Hello, Alice!
    #
    # 🚩Специальные методы (Special Methods или Magic Methods)
    #
    # Специальные методы определяют поведение объектов при
    # использовании встроенных функций и операций. Они включают
    # такие методы, как init, str, repr, len, getitem, setitem,
    # delitem, call, enter, exit, и многие другие.
    #
    # 🟠init
    # Конструктор класса, вызываемый при создании нового
    # экземпляра.
    #         class MyClass:
    #         def init(self, value):
    #             self.value = value
    #
    #     obj = MyClass(10)
    #
    #
    # 🟠str
    # Определяет строковое представление объекта для функции str()
    # и оператора print.
    #         class MyClass:
    #         def init(self, value):
    #             self.value = value
    #
    #         def str(self):
    #             return f"MyClass with value: {self.value}"
    #
    #     obj = MyClass(10)
    #     print(obj)  # Вывод: MyClass with value: 10
    #
    # 🟠__getitem__, __setitem__, __delitem__
    # Определяют поведение объекта при доступе к элементам по
    # индексу (для коллекций).
    #     class MyList:
    #         def __init__(self, items):
    #             self.items = items
    #
    #         def __getitem__(self, index):
    #             return self.items[index]
    #
    #         def __setitem__(self, index, value):
    #             self.items[index] = value
    #
    #         def __delitem__(self, index):
    #             del self.items[index]
    #
    #     lst = MyList([1, 2, 3])
    #     print(lst[1])  # Вывод: 2
    #     lst[1] = 20
    #     print(lst[1])  # Вывод: 20
    #     del lst[1]
    #     print(lst.items)  # Вывод: [1, 3]
    #
    #
    # 🟠__enter__, __exit__
    # Определяют поведение объекта в контексте оператора with.
    #     ```python
    #     class ManagedResource:
    #         def enter(self):
    #             print("Entering the context")
    #             return self
    #
    #         def exit(self, exc_type, exc_value, traceback):
    #             print("Exiting the context")
    #             return False
    #
    #     with ManagedResource():
    #         print("Inside the context")

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Class_07_ ()
#endif

#endmodule
