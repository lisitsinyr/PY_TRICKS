#------------------------------------------
# Strings_string01_method_encode ():
#------------------------------------------
def Strings_string01_method_encode ():
    """Strings_string01_method_encode"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method_encode.__name__}')
    print (f'#-----------------------------')

    # Строковый метод Python encode()
    # https://www.programiz.com/python-programming/methods/string/encode

    # В этом руководстве мы изучим метод Python encode() на практике. Этот строковый метод возвращает закодированную версию заданной строки.
    #
    # Пример:
    #
    # title = 'Python Programming'
    # # change encoding to utf-8
    # print(title.encode())
    # # Output: b'Python Programming'
    # Префикс “b” перед строкой указывает на то, что строка является байтовой строкой (bytes). Она представляет собой последовательность байтов, в отличие от обычной строковой переменной, которая содержит символы Unicode.
    #
    # Синтаксис метода encode()
    # Синтаксис метода encode() следующий:
    #
    # string.encode(encoding='UTF-8',errors='strict')
    # По умолчанию метод encode() не требует никаких параметров. При этом он возвращает закодированную версию строки в формате UTF-8. В случае неудачи он вызывает исключение UnicodeDecodeError.
    #
    # Однако encode() может принимать два параметра:
    #
    # encoding – тип кодировки, в которую должна быть закодирована строка.
    # errors – ответ при неудачном кодировании. Существует шесть типов ответа на ошибку:
    # strict – ответ по умолчанию, который при ошибке вызывает исключение UnicodeDecodeError
    # ignore – игнорирует некодируемый юникод из результата
    # replace – заменяет некодируемый символ на вопросительный знак
    # xmlcharrefreplace – вставляет ссылку на символ XML вместо некодируемого юникода
    # backslashreplace – символы, которые не могут быть представлены в кодировке, будут заменены последовательностями обратного слэша и шестнадцатеричных значений их кодов.
    # namereplace – символы, которые не могут быть представлены в кодировке, будут заменены специальными именованными последовательностями эскейп-символов.
    # Пример 1: Кодирование в UTF-8 по умолчанию
    # # unicode string
    # string = 'pythön!'
    # # print string
    # print('The string is:', string)
    # # default encoding to utf-8
    # string_utf = string.encode()
    # # print result
    # print('The encoded version is:', string_utf)
    # Вывод:
    #
    # The string is: pythön!
    # The encoded version is: b'pyth\xc3\xb6n!'
    # Пример 2: Кодирование с параметром errors
    # # unicode string
    # string = 'pythön!'
    # # print string
    # print('The string is:', string)
    # # ignore error
    # print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))
    # # replace error
    # print('The encoded version (with replace) is:', string.encode("ascii", "replace"))
    # Вывод:
    #
    # The string is: pythön!
    # The encoded version (with ignore) is: b'pythn!'
    # The encoded version (with replace) is: b'pyth?n!'
    # Примечание: попробуйте также различные сочетания параметров кодировки и ошибок.
    #
    # Кодировка строк
    # Начиная с Python 3.0, строки хранятся как Unicode, т.е. каждый символ в строке представлен кодовым символом. Таким образом, каждая строка – это просто последовательность кодовых символов Unicode.
    #
    # Для эффективного хранения этих строк последовательность кодовых символов преобразуется в набор байтов. Этот процесс известен как кодирование.
    #
    # Существуют различные кодировки, которые по-разному обрабатывают строку. Популярными кодировками являются UTF-8, ASCII и т.д. Используя метод string.encode(), вы можете преобразовать строки Unicode в любую кодировку, поддерживаемую Python. По умолчанию Python использует кодировку UTF-8.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method_encode ()
#endif

#endmodule
