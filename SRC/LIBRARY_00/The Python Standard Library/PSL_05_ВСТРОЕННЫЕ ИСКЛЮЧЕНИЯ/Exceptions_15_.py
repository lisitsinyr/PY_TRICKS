#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/Python_libr/1934
    # 📌 Иерархия ошибок
    #
    # Встроенные ошибки наследуются от Exception, их
    # «родственность» вы видите на фотографии.
    #
    # Если поставить except LookupError раньше чем except
    # IndexError, то второй обработчик никогда не сработает,
    # ошибку обработает первый except.
    #
    # Поэтому важно знать к какому типу какие ошибки относятся и
    # не ставить except OSError поверх FileExistsError.
    #
    # BaseException
    #
    # Attribute | [Arithmetic
    # Error Error
    #
    # FloatingPoint | [Overfiow
    # Error Error

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
