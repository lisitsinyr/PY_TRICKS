#------------------------------------------
# Strings_string01_method_find ():
#------------------------------------------
def Strings_string01_method_find ():
    """Strings_string01_method_find"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method_find.__name__}')
    print (f'#-----------------------------')

    # https://t.me/python_practics/2246
    # Замена текста другим текстом
    #
    # В данном примере используется метод replace() для замены
    # подстроки в строке. Исходная строка "python is a programming
    # language. python is python" содержит два вхождения слова
    # "python". После выполнения метода replace("python", 'Java'),
    # все вхождения слова "python" заменяются на "Java". В
    # результате получается строка "Java is a programming
    # language. Java is Java". Этот метод удобно использовать для
    # замен текста в строках.
    #
    # "python is a programming language. python is python".replace("python", 'Java' )
    # > Java is a programming language. Java is Java

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method_find ()
#endif

#endmodule
