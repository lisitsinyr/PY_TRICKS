#------------------------------------------
# f_strings_f_strings04_repr ():
#------------------------------------------
def f_strings_f_strings04_repr ():
    """f_strings_f_strings04_repr"""
#beginfunction
    print ('#-----------------------------')
    print ('#', f_strings_f_strings04_repr.__name__)
    print ('#-----------------------------')

    #------------------------------------------
    #
    #------------------------------------------
    from dataclasses import dataclass
    @dataclass
    class Person:
        name : str
        age : int
    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'
    Elon = Person("Elon Musk", 51)
    print(f'{Elon}')        # str
    print(f'{Elon!r}')      # repr

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f_strings_f_strings04_repr ()
#endif

#endmodule
