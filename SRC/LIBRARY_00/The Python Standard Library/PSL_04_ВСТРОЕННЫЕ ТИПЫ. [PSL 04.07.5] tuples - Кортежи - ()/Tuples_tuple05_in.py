#------------------------------------------
# Tuples_tuple05_in ():
# Используйте оператор in для проверки нахождения элемента в кортеже
#------------------------------------------
def Tuples_tuple05_in ():
    """Tuples_tuple05_in"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Tuples_tuple05_in.__name__}')
    print (f'#-----------------------------')

    ## 05.Проверка принадлежности элемента
    # Чтобы проверить, принадлежит ли элемент кортежу, используется оператор in. Если элемент присутствует в кортеже, оператор возвращает True, в противном случае — False.

    my_tuple = (1, 2, 3, 4, 5)
    # Проверка, содержится ли число 3 в кортеже
    print(3 in my_tuple)  # Вывод: True

    my_tuple = (1, 2, 3)

    is_present = 2 in my_tuple
    print (is_present)  # : True

    is_not_present = 4 not in my_tuple
    print (is_not_present)  # : True
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Tuples_tuple05_in ()
#endif

#endmodule
