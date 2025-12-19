#------------------------------------------
# Strings_string01_method_find ():
#------------------------------------------
def Strings_string01_method_find ():
    """Strings_string01_method_find"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method_find.__name__}')
    print (f'#-----------------------------')

    # Метод find() встроен в стандартный Python. Для поиска строки достаточно вызвать этот метод на объекте string, например, так: "string to search".find("search").
    # Метод find() ищет строку запроса и возвращает позицию первого символа, если искомая строка найдена. Если она не найдена, возвращается -1. Вы можете добавить начальный и конечный индекс: find(query, start, end), но эти параметры необязательны.
    s = "That I ever did see. Dusty as the handle on the door"
    index = s.find("Dusty")
    print(index)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method_find ()
#endif

#endmodule
