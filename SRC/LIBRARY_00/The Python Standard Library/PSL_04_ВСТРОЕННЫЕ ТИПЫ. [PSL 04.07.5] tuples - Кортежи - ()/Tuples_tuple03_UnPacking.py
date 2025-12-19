#------------------------------------------
# Tuples_tuple03_UnPacking ():
#------------------------------------------
def Tuples_tuple03_UnPacking ():
    """Tuples_tuple03_UnPacking"""
#beginfunction
    print ('#-----------------------------')
    print (f'# {Tuples_tuple03_UnPacking.__name__}')
    print ('#-----------------------------')

    ## 03.Упаковка и распаковка
    # Упаковка (packing) и распаковка (unpacking) — это операции,
    # которые позволяют создавать кортеж из набора значений и извлекать
    # значения из кортежа в переменные. Рассмотрим их подробнее.
    
    my_tuple = 1, 2, 3, 'hello'
    print(my_tuple)
    # Распаковка кортежа. Элементы кортежа извлекаются в переменные:
    a, b, c, d = my_tuple
    # Теперь переменные a, b, c, d содержат значения из кортежа
    # a = 1, b = 2, c = 3, d = 'hello'
    print(a) # : 1
    print(b) # : 2
    print(c) # : 3
    print(c) # : 'hello'

    my_tuple = (10, 20, 30)
    print(my_tuple)
    # распаковка кортежа
    a, b, c = my_tuple
    print(a) # : 10
    print(b) # : 20
    print(c) # : 30
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Tuples_tuple03_UnPacking ()
#endif

#endmodule
