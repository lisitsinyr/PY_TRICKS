#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/pyth0n_er/702
    # 🐍Нормализация в Python
    #
    # Нормализация - это полноценное приведение текста к единому
    # представлению.
    #
    # В данном примере sing1 - это «микрознак», а sing2 -
    # греческая строчная буква «мю».
    #
    # Интерпретатор Python'a видит эти символы как два разных, но
    # в стандарте Unicode они имеют одинаковое отображение.
    # Метод casefold() нормализовал переменную sing1 (перевел к
    # нижнему регистру и сконвертировал в Unicode форму).
    # import unicodedata
    #
    # sing1 = "yu" # MICRO SIGN
    #
    # | sing2 = "u" # GREEK SMALL LETTER MU
    # print (unicodedata.name(sing1) )
    #
    # | print (unicodedata.name(sing2) )
    #
    # print(singl == sing2)
    # # False
    #
    # print(sing1.casefold() == sing2.casefold() )
    # #True

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
