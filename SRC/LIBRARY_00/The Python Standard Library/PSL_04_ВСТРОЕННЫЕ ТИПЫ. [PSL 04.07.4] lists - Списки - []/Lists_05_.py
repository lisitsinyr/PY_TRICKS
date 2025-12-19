#------------------------------------------
# Lists_list01_Expand ():
#------------------------------------------
def Lists_list01_Expand ():
    """Lists_list01_Expand"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Lists_list01_Expand.__name__}')
    print (f'#-----------------------------')

    # https://t.me/python_easy_ru/1174
    # 🤔 Как разбить список?
    #
    # Разбить список (list) можно разными способами в зависимости
    # от задачи:
    # На части фиксированной длины
    # На N частей
    # По условию
    #
    # 🚩Разбить список на части фиксированного размера
    #
    # Если нужно разделить список на подсписки длиной n, можно
    # использовать list comprehension
    # def split_list(lst, size):
    #     return [lst[i:i + size] for i in range(0, len(lst),
    # size)]
    #
    # data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(split_list(data, 3))
    #
    # Вывод
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #
    # 🚩Разбить список на N частей (равных или почти равных)
    #
    # Если нужно разделить список на N частей, можно использовать
    # numpy или itertools
    # import numpy as np
    #
    # def split_into_n_parts(lst, n):
    #     return np.array_split(lst, n)
    #
    # data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(split_into_n_parts(data, 4))
    #
    # Вывод
    # [array([1, 2, 3]), array([4, 5]), array([6, 7]), array([8,
    # 9])]
    #
    # 🚩Разбить список по условию
    #
    # Если нужно разделить список по какому-то критерию, например,
    # на чётные и нечётные числа
    # data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #
    # even = [x for x in data if x % 2 == 0]
    # odd = [x for x in data if x % 2 != 0]
    #
    # print(even, odd)
    #
    # Вывод
    # [2, 4, 6, 8] [1, 3, 5, 7, 9]

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Lists_list01_Expand ()
#endif

#endmodule
