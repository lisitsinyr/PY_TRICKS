#------------------------------------------
# Tuples_tuple06_for_while ():
#------------------------------------------
def Tuples_tuple06_for_while ():
    """Tuples_tuple06_for_while"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Tuples_tuple06_for_while.__name__}')
    print (f'#-----------------------------')

    ## 06.Перебор элементов
    # Для перебора элементов кортежа в Python используется цикл for или while:

    my_tuple = (1, 2, 3, 4, 5)

    ### Перебор элементов кортежа с помощью цикла for
    for element in my_tuple:
        print(element)
    # Вывод:
    # 1
    # 2
    # 3
    # 4
    # 5

    ### Перебор элементов кортежа с помощью цикла while
    i = 0
    while i < len(my_tuple):
        print(my_tuple[i])
        i += 1
    # Код выводит каждый элемент кортежа my_tuple на новой строке.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Tuples_tuple06_for_while ()
#endif

#endmodule
