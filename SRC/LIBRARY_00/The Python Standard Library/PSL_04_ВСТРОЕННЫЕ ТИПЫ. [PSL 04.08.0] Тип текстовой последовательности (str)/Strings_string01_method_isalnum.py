#------------------------------------------
# Strings_string01_method_isalnum ():
#------------------------------------------
def Strings_string01_method_isalnum ():
    """Strings_string01_method_isalnum"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method_isalnum.__name__}')
    print (f'#-----------------------------')

    # Функция isalnum() используется для проверки, состоит ли строка из буквенно-цифровых символов.
    # Функция принимает в качестве аргумента строку и возвращает True,
    # если строка состоит только из буквенных символов (a-z, A-Z) и цифр (0-9), или False,
    # если в строке есть другие символы, пробелы, знаки пунктуации и т. д.
    stringl = "Hello123"
    print (stringl.isalnum ())  # True
    string2 = "Hello 123"
    print (string2.isalnum ())  # False, ecTb npoben
    string3 = "Hello@"
    print (string3.isalnum ())  # False, ecTb @


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method_isalnum ()
#endif

#endmodule
