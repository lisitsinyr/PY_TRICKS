#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/python_easy_ru/1019
    # 🤔 Расскажи о методах getitem и setitem и delitem?
    #
    # Методы getitem, setitem и delitem являются специальными
    # методами, которые позволяют пользовательским объектам
    # взаимодействовать с операциями получения, установки и
    # удаления элементов по индексу или ключу. Эти методы
    # обеспечивают интеграцию пользовательских классов с
    # операциями индексирования, делая их поведение аналогичным
    # встроенным типам данных, таким как списки и словари.
    #
    # 🚩Метод getitem
    #
    # Используется для получения значения элемента по индексу или
    # ключу. Он вызывается, когда используется оператор
    # индексирования (obj[key]).
    # class CustomList:
    #     def __init__(self, items):
    #         self.items = items
    #
    #     def __getitem__(self, index):
    #         return self.items[index]
    #
    # # Использование
    # my_list = CustomList([1, 2, 3, 4, 5])
    # print(my_list[2])  # Вывод: 3
    #
    # 🚩Метод titem и delit
    #
    # Используется для установки значения элемента по индексу или
    # ключу. Он вызывается, когда используется оператор
    # присваивания с индексированием (obj[key] = value).
    # class CustomList:
    #     def __init__(self, items):
    #         self.items = items
    #
    #     def __setitem__(self, index, value):
    #         self.items[index] = value
    #
    # # Использование
    # my_list = CustomList([1, 2, 3, 4, 5])
    # my_list[2] = 10
    # print(my_list.items)  # Вывод: [1, 2, 10, 4, 5]
    #
    # 🚩Метод delitem
    #
    # Используется для удаления элемента по индексу или ключу. Он
    # вызывается, когда используется оператор удаления с
    # индексированием (del obj[key]).
    # class CustomList:
    #     def __init__(self, items):
    #         self.items = items
    #
    #     def __delitem__(self, index):
    #         del self.items[index]
    #
    # # Использование
    # my_list = CustomList([1, 2, 3, 4, 5])
    # del my_list[2]
    # print(my_list.items)  # Вывод: [1, 2, 4, 5]
    #
    # Полный пример пользовательского класса
    # class CustomDict:
    #     def __init__(self):
    #         self.items = {}
    #
    #     def __getitem__(self, key):
    #         return self.items[key]
    #
    #     def __setitem__(self, key, value):
    #         self.items[key] = value
    #
    #     def __delitem__(self, key):
    #         del self.items[key]
    #
    #     def __repr__(self):
    #         return f"{self.items}"
    #
    # # Использование
    # my_dict = CustomDict()
    # my_dict['a'] = 1
    # my_dict['b'] = 2
    # print(my_dict['a'])  # Вывод: 1
    # print(my_dict)       # Вывод: {'a': 1, 'b': 2}
    # del my_dict['a']
    # print(my_dict)       # Вывод: {'b': 2}

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
