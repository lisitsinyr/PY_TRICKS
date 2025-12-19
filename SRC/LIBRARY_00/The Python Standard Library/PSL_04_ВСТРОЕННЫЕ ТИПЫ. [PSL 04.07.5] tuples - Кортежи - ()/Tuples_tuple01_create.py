#------------------------------------------
# tuples_tuple01_create () -> None:
# Создание кортежа
#------------------------------------------
def tuples_tuple01_create () -> None:
    """Tuples_tuple_create"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {tuples_tuple01_create.__name__}')
    print (f'#-----------------------------')

    ## 01. Создание кортежа
    # Создать кортеж в Python можно по меньшей мере пятью способами

    # 1. С помощью круглых скобок:
    print (f'1.С помощью круглых скобок:')
    my_tuple = (1, 2, 3, 'a', 'b', 'c')
    print (f'{my_tuple=}')
    print (f'')

    # 2. Без круглых скобок:
    print (f'2.Без круглых скобок:')
    my_tuple = 1, 2, 3, 'a', 'b', 'c'
    print (f'{my_tuple=}')
    print (f'')

    # 3. Используя встроенную функцию tuple():
    my_tuple = tuple([1, 2, 3, 'a', 'b', 'c'])
    print (f'{my_tuple=}')
    print (f'')

    # 4. С помощью оператора упаковки
    print (f'4.С помощью оператора упаковки')
    a = 1
    b = 2
    c = 3
    my_tuple = a, b, c  # Эквивалентно (a, b, c)
    print (f'{my_tuple=}')
    print (f'')

    # 5. Из итерируемого элемента, например строки, с помощью функции tuple():
    print (f'5.Из итерируемого элемента, например строки, с помощью функции tuple():')
    my_tuple = tuple('hello')
    # Результат: ('h', 'e', 'l', 'l', 'o')
    print (f'{my_tuple=}')
    print (f'')

    print (f'Кортеж из чисел, в том числе с плавающей точкой и комплексных')
    tuple_numbers = (1, 2, 3, 4, 5, 2.5, 3 + 4j)
    print (f'{tuple_numbers=}')
    print (f'')

    print (f'Кортеж из строк')
    tuple_strings = ('яблоко', 'банан', 'апельсин')
    print (f'{tuple_strings=}')
    print (f'')

    print (f'Кортеж из логических значений')
    tuple_bools = (True, False)
    print (f'{tuple_bools=}')
    print (f'')

    print (f'Кортеж из других кортежей')
    tuple_tuples = ((1, 2), ('a', 'b'))
    print (f'{tuple_tuples=}')
    print (f'')

    print (f'Кортеж из списков')
    tuple_lists = ([1, 2, 3], ['a', 'b', 'c'])
    print (f'{tuple_lists=}')
    print (f'')

    print (f'Кортеж из словарей')
    tuple_dicts = ({'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25})
    print (f'{tuple_dicts=}')
    print (f'')

    print (f'Кортеж из разных типов данных')
    tuple_mixed = (1, 'hello', [1, 2, 3], {'a': 10})
    print (f'{tuple_mixed=}')
    print (f'')

    # Пустой кортеж
    print (f'Пустой кортеж')
    tuple_empty_1 = ()
    print (f'{tuple_empty_1}')
    tuple_empty_2 = ()
    print (f'{tuple_empty_2}')
    print (f'')

    # кортеж, состоящий всего из одного элемента
    print (f'Кортеж из одного элемента')
    tuple_one_1 = ('s', )
    print (f'{tuple_one_1}')
    tuple_one_2 = 's',
    print (f'{tuple_one_2}')
    print (f'')
    # после элемента необходимо обязательно поставить запятую:
    tuple_one_3 = (42,)
    print (f'{tuple_one_3}')
    # Или так
    tuple_one_4 = 42,
    print (f'{tuple_one_4}')

    # Если запятую не поставить, то получим объект типа int
    tuple_one_5 = (42)
    print (f'{tuple_one_5}')
    print (f'')

    print (f'Создание кортежа из списка')
    tuple_from_list = tuple ([4, 5, 6])
    print (f'{tuple_from_list=}')
    print (f'')
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    tuples_tuple01_create ()
#endif

#endmodule
