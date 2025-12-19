#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/python_easy_ru/1006
    # 🤔 Что такое JSON?
    #
    # Это легковесный формат обмена данными, который легко
    # читается и пишется человеком, а также легко парсится и
    # генерируется машинами. JSON используется для передачи данных
    # между клиентом и сервером, особенно в веб-приложениях.
    #
    # 🚩Основные характеристики
    #
    # 🟠Простота и легкость
    # JSON простой и легкий для понимания, что делает его удобным
    # для обмена данными.
    #
    # 🟠Является текстовым форматом
    # JSON представлен в текстовом формате, что позволяет легко
    # его читать и отлаживать.
    #
    # 🟠Язык-независимость
    # Хотя JSON основан на подмножестве языка JavaScript, он
    # поддерживается многими языками программирования, включая
    # Python, Java, C#, PHP и другие.
    #
    # 🚩JSON состоит из двух основных структур
    #
    # 🟠Объекты
    # Набор пар "ключ-значение", заключенный в фигурные скобки {}.
    # Ключи должны быть строками, а значения могут быть различными
    # типами данных.
    # 🟠Массивы
    # Упорядоченные списки значений, заключенные в квадратные
    # скобки [].
    # {
    #     "name": "John Doe",
    #     "age": 30,
    #     "isStudent": false,
    #     "courses": ["Math", "Science", "History"],
    #     "address": {
    #         "street": "123 Main St",
    #         "city": "Anytown",
    #         "zip": "12345"
    #     }
    # }
    #
    # 🚩Типы данных
    #
    # 🟠Строки
    # Последовательности символов, заключенные в двойные кавычки.
    # "name": "John Doe"
    #
    # 🟠Числа
    # Целые числа и числа с плавающей запятой.
    # "age": 30
    #
    # 🟠Булевы значения
    # true или false.
    # "isStudent": false
    #
    # 🟠Массивы
    # Упорядоченные списки значений.
    # "courses": ["Math", "Science", "History"]
    #
    # 🟠Объекты
    # Наборы пар "ключ-значение".
    # "address": {
    #     "street": "123 Main St",
    #     "city": "Anytown",
    #     "zip": "12345"
    # }
    #
    # 🟠Null
    # Значение null.
    # "middleName": null
    #
    # Преобразование Python объектов в JSON (сериализация)
    # import json
    #
    # data = {
    #     "name": "John Doe",
    #     "age": 30,
    #     "isStudent": False,
    #     "courses": ["Math", "Science", "History"],
    #     "address": {
    #         "street": "123 Main St",
    #         "city": "Anytown",
    #         "zip": "12345"
    #     }
    # }
    #
    # # Преобразование Python объекта в JSON строку
    # json_string = json.dumps(data, indent=4)
    # print(json_string)
    #
    # Преобразование JSON в Python объекты (десериализация)
    # import json
    #
    # json_string = '''
    # {
    #     "name": "John Doe",
    #     "age": 30,
    #     "isStudent": false,
    #     "courses": ["Math", "Science", "History"],
    #     "address": {
    #         "street": "123 Main St",
    #         "city": "Anytown",
    #         "zip": "12345"
    #     }
    # }
    # '''
    #
    # # Преобразование JSON строки в Python объект
    # data = json.loads(json_string)
    # print(data)
    # print(data['name'])  # John Doe
    #
    # 🚩Пример чтения и записи JSON в файл
    #
    # Запись JSON в файл
    # import json
    #
    # data = {
    #     "name": "John Doe",
    #     "age": 30,
    #     "isStudent": False,
    #     "courses": ["Math", "Science", "History"],
    #     "address": {
    #         "street": "123 Main St",
    #         "city": "Anytown",
    #         "zip": "12345"
    #     }
    # }
    #
    # with open('data.json', 'w') as file:
    #     json.dump(data, file, indent=4)
    #
    # Чтение JSON из файла
    # import json
    #
    # with open('data.json', 'r') as file:
    #     data = json.load(file)
    #     print(data)
    #     print(data['name'])  # John Doe

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
