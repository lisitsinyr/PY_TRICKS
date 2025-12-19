#------------------------------------------
# Class_03_ ():
#------------------------------------------
def Class_03_ ():
    """Class_03_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Class_03_.__name__)
    print ('#-----------------------------')

    # https://t.me/pyth0n_er/775
    # ➡️В Python абстрактный класс реализуется с помощью модуля
    # abc (Abstract Base Classes).
    #
    # ⬆️В данном примере класс Animal является абстрактным, так
    # как содержит абстрактный метод speak. Классы Dog и Cat
    # наследуются от класса Animal и реализуют метод speak. Класс
    # Animal нельзя инстанциировать напрямую, он служит лишь
    # базовым классом для других классов.
    #
    # from abc import ABC, abstractmethod
    #
    # class Animal(ABC):
    # @abstractmethod
    # def speak(self):
    # pass
    #
    # class Dog(Animal):
    #
    # def speak(self):
    # print("Woof")
    #
    # class Cat(Animal):
    # def speak(self):
    #
    # print("Meow")
    #
    # dog = Dog()
    # cat = Cat()
    #
    # dog.speak()
    # cat.speak()

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Class_03_ ()
#endif

#endmodule
