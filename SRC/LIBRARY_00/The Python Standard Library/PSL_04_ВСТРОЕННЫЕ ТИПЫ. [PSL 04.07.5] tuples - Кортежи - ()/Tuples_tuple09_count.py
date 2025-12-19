#------------------------------------------
# Tuples_tuple09_count ():
# Метод count() возвращает количество вхождений указанного значения в кортеже
#------------------------------------------
def Tuples_tuple09_count ():
    """Tuples_tuple09_count"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Tuples_tuple09_count.__name__}')
    print (f'#-----------------------------')

    ## 09. Функции кортежей Python
    # В Python есть встроенные функции, которые облегчают работу с кортежами.
    # tuple.count(x) Возвращает количество элементов со значением x, если нет значения возвращает 0
    my_tuple = (1, 2, 3, 2, 2)
    count_of_twos = my_tuple.count (2)
    print (count_of_twos)  # : 3

#endfunction


#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Tuples_tuple09_count ()
#endif

#endmodule
