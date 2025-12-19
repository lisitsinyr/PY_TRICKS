#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Link: https://t.me/python_easy_ru/1396
    #
    # Дата: 2025-05-19 13:05:08
    #
    # Title: Python | Вопросы собесов
    #
    # username: python_easy_ru
    #
    # 🤔 Cловари {dict}?
    #
    # Словарь (dict) — это структура данных, которая хранит пары
    # "ключ → значение".
    #
    # 🟠Создание словаря
    # Через {} (фигурные скобки)
    # my_dict = {"name": "Alice", "age": 25, "city": "New York"}
    #
    # Изменение значения
    # my_dict["age"] = 26  # Меняем возраст
    #
    # del — удаление по ключу
    # del my_dict["city"]
    #
    # Перебор ключей (for key in dict)
    # for key in my_dict:
    #     print(key, my_dict[key])
    #
    # Проверка наличия ключа
    # if "name" in my_dict:
    #     print("Ключ существует!")
    #
    # 🟠Генерация словарей (Dictionary Comprehension)
    # Создадим словарь квадратов чисел
    # squares = {x: x**2 for x in range(1, 6)}
    # print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    #
    # 🟠Ключи должны быть хешируемыми (неизменяемыми)
    # Нельзя использовать list как ключ!
    # my_dict[[1, 2, 3]] = "Ошибка"  # TypeError: unhashable type:
    # 'list'
    #
    # Можно использовать tuple, int, str, frozenset
    # my_dict[(1, 2, 3)] = "OK"

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
