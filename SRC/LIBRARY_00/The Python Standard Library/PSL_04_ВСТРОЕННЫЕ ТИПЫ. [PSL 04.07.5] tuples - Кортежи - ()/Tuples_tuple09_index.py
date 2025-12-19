#------------------------------------------
# Tuples_tuple09_index ():
#------------------------------------------
def Tuples_tuple09_index ():
    """Tuples_tuple09_index"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Tuples_tuple09_index.__name__}')
    print (f'#-----------------------------')

    ## 09. Функции кортежей Python
    # В Python есть встроенные функции, которые облегчают работу с кортежами.
    # tuple.index(x, [start [, end]]) # Возвращает положение(индекс) первогоэлемента со значением x (при этом поиск ведется от start до end)
    my_tuple = (1, 2, 3, 2, 2)
    index_of_two = my_tuple.index (2)
    print (index_of_two)  # : 1
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Tuples_tuple09_index ()
#endif

#endmodule
