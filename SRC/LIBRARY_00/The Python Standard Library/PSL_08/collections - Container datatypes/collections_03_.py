#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # ​ (http://api.channely.co/file/c84e8a39e9b14fa0a2ecdfee0e0d
    # 503f)Counter: подсчёт числа элементов в списке
    #
    # Помимо способности collections.Counter() понимать, что
    # именно в строке нужно подсчитать:
    #
    # from collections import Counter
    #
    # Counter("mississippi")
    # >>> Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
    #
    # в случае со списком слов модуль автоматически рассчитает,
    # как часто встречается тот или иной элемент:
    #
    # party_list = ["Alice", "Bob", "Alice", "Eve", "Bob", "Eve",
    # "Alice"]
    # print(Counter(party_list))
    # >>> Counter({'Alice': 3, 'Bob': 2, 'Eve': 2})

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
