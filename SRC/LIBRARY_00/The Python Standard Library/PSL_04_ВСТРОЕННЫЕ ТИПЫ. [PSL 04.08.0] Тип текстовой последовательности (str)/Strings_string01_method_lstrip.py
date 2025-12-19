#------------------------------------------
# Strings_string01_method_lstrip ():
#------------------------------------------
def Strings_string01_method_lstrip ():
    """Strings_string01_method_lstrip"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method_lstrip.__name__}')
    print (f'#-----------------------------')

    # lstrip() возвращает копию строки с удаленными ведущими символами.
    # Все комбинации символов в аргументе chars удаляются слева от строки до первого несоответствия.
    # Если аргумент chars не указан, все ведущие пробелы удаляются из строки.

    random_string = '   this is good '
    print(random_string.lstrip())
    #_this is good
    print(random_string.lstrip('sti'))
    #_    this is good
    print(random_string.lstrip('s ti'))
    #_his is good

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method_lstrip ()
#endif

#endmodule
