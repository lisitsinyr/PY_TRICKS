#------------------------------------------
# Emulating_numeric_01_ ():
#------------------------------------------
def Emulating_numeric_01_ ():
    """Emulating_numeric_01_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Emulating_numeric_01_.__name__)
    print ('#-----------------------------')


    # https://t.me/pythonl/4365
    # 🖥 Указание арифметических операции вручную между объектами
    # класса может сделать код менее читабельным.
    #
    # Метод _add__ в Python обеспечивает изящный арифметический
    # синтаксис между вашими объектами класса и делает код более
    # читабельным и интуитивно понятным.

    class Animal:
        def __init__(self, species: str, weight: float):
            self.species = species
            self.weight = weight
    lion = Animal("Lion", 200)
    tiger = Animal("Tiger", 180)
    total_weight = lion.weight + tiger.weight
    print (total_weight)

    class Animal:
        def __init__(self, species: str, weight: float):
            self.species = species
            self.weight = weight
        def __add__(self, other):
            return Animal(
        f"{self.species}+{other.species}",
                self.weight + other.weight
            )
    lion = Animal("Lion", 200)
    tiger = Animal("Tiger", 180)
    combined = lion + tiger
    print (combined.weight) # 3

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Emulating_numeric_01_ ()
#endif

#endmodule
