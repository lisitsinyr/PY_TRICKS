#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/pyth0n_er/566
    # 🐍collections.MutableMapping
    #
    # Collections.MutableMapping — это интерфейс, который
    # представляет изменяемое отображение (словарь).
    # Он наследуется от интерфейса Mapping и добавляет методы для
    # изменения отображения, такие как __setitem__, __delitem__ и
    # clear.
    #
    # ❗Основное преимущество в использовании MutableMapping — это
    # возможность передавать экземпляры такого класса в любое API,
    # ожидающее словарь.
    # Например, во многих функциях в стандартной библиотеке есть
    # параметры типа dict. Если создать класс, реализующий
    # MutableMapping, его экземпляры можно будет передавать в
    # такие функции.
    #
    # from collections.abc import MutableMapping
    #
    # class CustomDict(MutableMapping):
    #
    # def __init__(self):
    # self.data = {}
    #
    # def __getitem__(self, key):
    # return self.data[key]
    #
    # def __setitem_(self, key, value):
    #
    # self.data[key] = value
    #
    # def __delitem_(self, key):
    # del self.data[key]
    #
    # def __iter__(self):
    #
    # return iter(self.data)
    #
    # def __len_(self):
    # return len(self.data)
    #
    # my_dict = CustomDict()
    # my_dict['foo'] = ‘bar'
    #
    # print(my_dict['foo'])
    # # selpegeTt ‘bar'
    #
    # my_dict['x'] = 10
    # print(my_dict['x'])
    #
    # # BeiBegeT 10
    #
    # del my_dict['foo']
    # # yaanut Koy 'foo' uz cnoBapa
    #
    # print(len(my_dict))
    #
    # # epipegeT 1, T.K. OCTaNcA TOMbKO 1 3NeMeHT

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
