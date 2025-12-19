#------------------------------------------
# Asynchronous Iterators_01_ ():
#------------------------------------------
def Asynchronous Iterators_01_ ():
    """Asynchronous Iterators_01_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Asynchronous Iterators_01_.__name__)
    print ('#-----------------------------')


    # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/aiter-sozdaet-asinhronnyj-iterator/
    #
    # Функция aiter() создает асинхронный итератор
    #
    # Справочник по языку Python3.
    # Встроенные функции Python
    # Функция aiter() создает асинхронный итератор
    # Синтаксис:
    # # Новое в версии 3.10.
    # aiter(async_iterable)
    # Параметры:
    # async_iterable - объект, который можно использовать в инструкции async for/in. Должен возвращать асинхронный итератор из своего метода __aiter__().
    # Возвращаемое значение:
    # асинхронный итератор. Объект, реализующий метод __anext__(), который возвращает awaitable объект, используемый совместно с инструкцией await.
    # Описание:
    # Функция aiter() возвращает асинхронный итератор для асинхронного итерирования по нему например в async for/in. Эквивалентно вызову x.__aiter__().
    #
    # Сама функция aiter(x) имеет метод __aiter__(), который возвращает x, поэтому вызов aiter(aiter(x)) совпадает с вызовом aiter(x).
    #
    # Примечание. В отличие от синхронной функции iter(), у aiter() нет варианта с двумя аргументами.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Asynchronous Iterators_01_ ()
#endif

#endmodule
