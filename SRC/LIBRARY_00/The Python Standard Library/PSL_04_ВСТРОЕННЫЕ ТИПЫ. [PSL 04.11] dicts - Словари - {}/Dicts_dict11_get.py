#------------------------------------------
# Dicts_dict11_get ():
#------------------------------------------
def Dicts_dict11_get ():
    """Dicts_dict11_get"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Dicts_dict11_get.__name__}')
    print (f'#-----------------------------')

    my_dict = {'a': 1, 'b': 2}
    # Скобки
    print(my_dict['c']) # Error (Owv6xa)
    # Get method
    print(my_dict.get('c')) # None

    dict_ = {'keyl1': 'valuel', 'key2': 'value2'}
    print (dict_.get ('key1'))  # ‘valuel’
    print (dict_.get ('key3'))  # None
    print (dict_.get ('key3', 'default'))  # ‘default’

    # Разберем два похожих метода для работы со словарями!
    # • get() — возвращает значение для указанного ключа, если
    # ключ находится в словаре. Если ключ не найден, метод вернет
    # None.
    my_dict = {'luppy': 'droopy'}
    key_1 = my_dict.get ('luppy')
    key_2 = my_dict.get ('droopy', 'Het tyT Takoro')
    print (key_1, key_2, sep = '\n')
    # • setdefault() — позволяет извлекать значение по указанному
    # ключу, если он существует. Если ключа нет, функция вставляет
    # ключ с указанным значением по умолчанию и возвращает это
    # значение
    my_dict = {'luppy': 'droopy'}
    my_dict.setdefault ('droopy', 'Luppy')
    print (my_dict)



#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Dicts_dict11_get ()
#endif

#endmodule
