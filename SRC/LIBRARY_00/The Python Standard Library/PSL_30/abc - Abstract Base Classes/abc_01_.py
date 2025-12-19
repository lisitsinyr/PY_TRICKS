#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/python_easy_ru/765
    # 🤔 Как создать абстрактный класс?
    #
    # Используется модуль abc (Abstract Base Classes). Абстрактный
    # класс не может быть инстанцирован и предназначен для
    # создания шаблонов, которые должны быть реализованы в
    # подклассах.
    #
    # 🚩Шаги
    #
    # 1⃣Импортирование модуля `abc`
    # Для использования абстрактных классов и методов нужно
    # импортировать модуль abc.
    # 2⃣Создание абстрактного класса
    # Абстрактный класс должен наследоваться от ABC (абстрактный
    # базовый класс), который предоставляется модулем abc.
    # 3⃣Определение абстрактных методов
    # Абстрактные методы обозначаются декоратором @abstractmethod.
    # Эти методы должны быть реализованы в подклассах, иначе они
    # тоже станут абстрактными.
    # from abc import ABC, abstractmethod
    #
    # # Создание абстрактного класса
    # class Animal(ABC):
    #
    #     @abstractmethod
    #     def make_sound(self):
    #         pass
    #
    #     @abstractmethod
    #     def move(self):
    #         pass
    #
    # # Попытка создания экземпляра абстрактного класса приведет к
    # ошибке
    # # animal = Animal()  # TypeError: Can't instantiate abstract
    # class Animal with abstract methods make_sound, move
    #
    # # Создание подклассов, которые реализуют абстрактные методы
    # class Dog(Animal):
    #     def make_sound(self):
    #         return "Woof"
    #
    #     def move(self):
    #         return "Runs"
    #
    # class Bird(Animal):
    #     def make_sound(self):
    #         return "Tweet"
    #
    #     def move(self):
    #         return "Flies"
    #
    # # Теперь можно создать экземпляры подклассов
    # dog = Dog()
    # print(dog.make_sound())  # Woof
    # print(dog.move())        # Runs
    #
    # bird = Bird()
    # print(bird.make_sound())  # Tweet
    # print(bird.move())        # Flies

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
