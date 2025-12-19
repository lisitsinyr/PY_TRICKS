#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/Python_libr/1933
    # 📌 Exception Chaining
    #
    # Это связывание нескольких ошибок в один traceback.
    # Используется, если при обработке исключения нужно добавить
    # информацию или изменить тип.
    #
    # Исключение, добавленное с raise ... from exc, сохраняется в
    # __cause__. Если ошибка произошла во время выполнения
    # try/except, то она запишется в __context__.
    #
    # 📕 PEP 3134
    #
    #  (https://peps.python.org/pep-3134)#урок
    #
    # filename "file.txt'
    #
    # try:
    # file = open( filename)
    #
    # except OSError as e:
    # message = f'something wrong with {filename}'
    # raise RuntimeError(message) from e


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
