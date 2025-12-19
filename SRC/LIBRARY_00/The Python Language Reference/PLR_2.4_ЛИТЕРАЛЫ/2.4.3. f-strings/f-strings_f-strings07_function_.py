# ------------------------------------------
# f_strings_f_strings07_function ():
# ------------------------------------------
def f_strings_f_strings07_function ():
    """f_strings_f_strings07_function"""
#beginfunction
    print ('#-----------------------------')
    print ('#', f_strings_f_strings07_function.__name__)
    print ('#-----------------------------')

    #------------------------------------------
    # You can execute functions inside the placeholder:
    #------------------------------------------
    fruit = "apples"
    txt = f'I love {fruit.upper ()}'
    print (txt)

    #------------------------------------------
    # Функции, lambda-функции и расчёты
    # Вы можете делать расчёты прямо внутри f-строк, а также использовать методы и функции, добавляя их внутрь фигурных скобок {}.
    #------------------------------------------
    # Function calls
    def double (x):
        return x * 2
    print (f'Double of 5 is {double (5)}')
    #------------------------------------------
    def foo ():
        return 10
    print (f'Результат: {foo ()}.')
    #------------------------------------------
    # The function does not have to be a built-in Python method, you can create your own functions and use them:
    #------------------------------------------
    def myconverter (x):
        return x * 0.3048
    txt = f'The plane is flying at a {myconverter (30000)} meter altitude'
    print (txt)

    #------------------------------------------
    # Расчёты:
    #------------------------------------------
    print (f'8 плюс 10 будет {8 + 10}.')

    #------------------------------------------
    # Методы:
    #------------------------------------------
    name = 'олег'
    print (f'Меня зовут {name.upper ()}.')

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f_strings_f_strings07_function ()
#endif

#endmodule
