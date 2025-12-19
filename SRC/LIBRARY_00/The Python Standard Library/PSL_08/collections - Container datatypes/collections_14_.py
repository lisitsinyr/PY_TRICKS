#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/pytstart/112
    # 🖥 OrderedDict – это упорядоченный словарь из модуля
    # collections, который сохраняет порядок добавления ключей (в
    # отличие от обычного dict в Python <3.7).
    #
    # 📌 Основные особенности:
    # ✔️ Запоминает порядок добавления элементов.
    # ✔️ Поддерживает все методы обычного dict.
    # ✔️ Имеет дополнительные методы: move_to_end(),
    # popitem(last=True).
    #
    # ➡️ Пример:
    #
    #
    # from collections import OrderedDict
    #
    # # Создаём OrderedDict
    # ordered_dict = OrderedDict()
    # ordered_dict["a"] = 1
    # ordered_dict["b"] = 2
    # ordered_dict["c"] = 3
    #
    # print(ordered_dict)  # OrderedDict([('a', 1), ('b', 2),
    # ('c', 3)])
    #
    # ➡️ Дополнительные методы:
    #
    #
    # ordered_dict.move_to_end("a")  # Переместит "a" в конец
    # print(ordered_dict)  # OrderedDict([('b', 2), ('c', 3),
    # ('a', 1)])
    #
    # ordered_dict.popitem()  # Удалит последний элемент ('a', 1)
    #
    # 📌 В Python 3.7+ обычный dict уже сохраняет порядок, но
    # OrderedDict всё ещё полезен, если нужны его специальные
    # методы.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
