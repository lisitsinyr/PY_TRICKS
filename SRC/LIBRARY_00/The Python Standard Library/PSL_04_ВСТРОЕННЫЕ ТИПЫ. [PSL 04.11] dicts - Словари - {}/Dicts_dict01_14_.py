#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Link: https://t.me/PythonPortal/4448
    #
    # Дата: 2025-06-02 06:07:00+00:00
    #
    # Title: Python Portal
    #
    # Нужно искать ключи в нескольких словарях с приоритетом?
    #
    # **Ручной способ поиска:** сначала в `group3`, если нет — в
    # `group2`, если и там нет — в `group1`:
    #
    # ```age = group3.get(name, group2.get(name,
    # group1.get(name)))```
    #
    # Работает, но нечитаемо и неудобно, особенно при большом
    # количестве словарей.
    #
    # Лучше используй `ChainMap` для чистой логики с подстановкой
    # по умолчанию
    #
    # ```m = ChainMap(group3, group2, group1)
    # age = m.get("ana")```
    #
    # Создается объект[ ](https://t.me/PythonPortal)ChainMap, который объединяет словари по приоритету:
    #
    # Просто вызываешь `m.get(key)` — он сам идет по цепочке, пока
    # не найдет ключ
    #
    # Даже если ключ есть в нескольких словарях, берётся первое
    # вхождение по приоритету
    #
    # from collections import ChainMap
    #
    # group1 = {'tim': 30, 'bob': 17, ‘ana': 24}
    # group2 = {'ana': 26, 'thomas': 64, ‘helen': 26}
    # group3 = {'brenda': 17, 'otto': 44, '‘thomas': 46}
    #
    # # X% Clunky manual fallback logic
    #
    # name = "ana"
    #
    # age = group3.get(name, group2.get(name, groupl.get(name) ) )
    # print(age) # 26 - from group2, overrides groupl
    #
    # # @ Clean and scalable with ChainMap
    #
    # m = ChainMap(group3, group2, group1)
    #
    # age = m.get("ana")
    #
    # print(age) # 26 > from group2, overrides groupl
    #
    # age = m.get("thomas" )
    # print(age) # 46 - from group3, overrides group2

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
