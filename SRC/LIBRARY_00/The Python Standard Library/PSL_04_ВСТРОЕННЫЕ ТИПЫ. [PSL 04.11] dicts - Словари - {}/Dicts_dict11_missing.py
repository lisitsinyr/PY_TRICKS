#------------------------------------------
# Dicts_dict11_missing ():
#------------------------------------------
def Dicts_dict11_missing ():
    """Dicts_dict11_missing"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Dicts_dict11_missing.__name__}')
    print (f'#-----------------------------')

    # Отсутствующие элементы словарей
    # В Python 2.5 у словарей появился специальный метод missing.
    # Он вызывается при обращении к отсутствующим элементам.
    # Примерно то же самое делает подкласс defaultdict: он
    # вызывает для несуществующих элементов функцию без
    # аргументов.
    from collections import defaultdict
    m = defaultdict (list)
    m ["foo"].append (1)
    m ["foo"].append (2)
    print (m)
    # {'foo': [1, 2]}

    # Если в словаре нет определённого ключа, то вызывается
    # __missing__. Суть в том, что мы можем переопределить этот
    # метод.
    # Примерно по такому принципу, как на фото выше, работает
    # defaultdict из модуля collections.
    class ListDict (dict):
        def __missing__(self, key):
            self [key] = value = []
            return value
    a = ListDict ()
    a ['foo'].append (1)
    a ['foo'].append (2)
    a ['bar'].append (3)
    print (a)

    #endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Dicts_dict11_missing ()
#endif

#endmodule
