#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/codeblog8/263
    # Добавляем логику в собственное исключение
    #
    # Исключение можно поднять с аргументом и без него. Когда мы
    # передаем аргумент, класс NetworkError подхватывает его и
    # запускает первое условие, как показано на экране.
    #
    # Вызов без аргументов, приведет к запуску условия else, что
    # выведет базовую информацию об ошибке. Здесь предоставлен
    # простой пример, однако можно добавить абсолютно любую
    # логику.
    #
    # class NetworkError(Exception) :
    # def __init__(self, xargs: object) -> None:
    # self.response = args[0] if args else None
    #
    # def __str__(self):
    # if self.response:
    # return f"Response: ({self.response})"
    # else:
    #
    # return "Oops..."
    # raise NetworkError("Hello World")
    #
    # # BbiBoo:
    #
    # # Traceback (most recent call last):
    #
    # # File "/home/user/test.py", line 14, in <module>
    # # raise NetworkError("Hello World")
    #
    # # NetworkError: Response: (Hello World)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
