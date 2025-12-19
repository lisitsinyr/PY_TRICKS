#------------------------------------------
# Strings_string01_method_count ():
#------------------------------------------
def Strings_string01_method_count ():
    """Strings_string01_method_count"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method_count.__name__}')
    print (f'#-----------------------------')

    # Метод .count() в Python используется для подсчета количества
    # вхождений определенного элемента в строке, списке или
    # кортеже. Синтаксис метода выглядит следующим образом:
    #
    # <obj>.count(<value>)
    #
    # ⬆️где <obj> - объект, в котором мы ищем, а <value> -
    # значение, которое мы хотим посчитать.
    #
    # ➡️Примеры использования метода .count()
    #
    # Давайте рассмотрим несколько примеров использования метода
    # .count().
    #
    # ➡️Подсчет количества символов в строке:
    #
    s = "Hello, World!"
    count = s.count("o")
    print(count)  # Output: 2
    #
    # ➡️Подсчет количества элементов в списке:
    #
    numbers = [1, 2, 3, 4, 2, 1, 2]
    count = numbers.count(2)
    print(count)  # Output: 3
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method_count ()
#endif

#endmodule
