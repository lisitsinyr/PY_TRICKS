#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/c/2383487131/221
    # 👨‍💻 Гайд: Как работать с JSON в Python. Часть 1
    #
    # JSON (JavaScript Object Notation) — это текстовый формат
    # обмена данными, который часто используется в API,
    # конфигурационных файлах и при работе с веб-приложениями. В
    # Python для работы с JSON используется встроенный модуль
    # json.
    #
    # 1️⃣ Чтение JSON-строк
    #
    # Вы можете загружать JSON-данные из строки с помощью функции
    # json.loads.
    #
    # import json
    #
    # # JSON-строка
    # data = '{"name": "Alice", "age": 25, "hobbies": ["reading",
    # "coding"]}'
    #
    # # Преобразуем строку в Python-словарь
    # parsed_data = json.loads(data)
    # print(parsed_data["name"])  # Alice
    # print(parsed_data["hobbies"])  # ['reading', 'coding']
    #
    # 2️⃣ Чтение JSON из файла
    #
    # Если JSON-данные хранятся в файле, используйте функцию
    # json.load.
    #
    # import json
    #
    # # Открываем файл с JSON
    # with open("data.json", "r") as file:
    #     data = json.load(file)
    #
    # # Работаем с данными
    # print(data["name"])  # Alice
    # print(data["age"])  # 25
    #
    # ➡️ Пример файла data.json:
    #
    # {
    #     "name": "Alice",
    #     "age": 25,
    #     "hobbies": ["reading", "coding"]
    # }
    #
    # 3️⃣ Запись JSON в файл
    #
    # Функция json.dump сохраняет данные Python в файл в формате
    # JSON.
    #
    # import json
    #
    # # Данные для записи
    # data = {
    #     "status": "success",
    #     "code": 200,
    #     "message": "Data saved successfully!"
    # }
    #
    # # Сохраняем в файл
    # with open("output.json", "w") as file:
    #     json.dump(data, file, indent=4)  # indent=4 делает JSON
    # читабельным
    #
    # ➡️ Результат в файле output.json:
    #
    # {
    #     "status": "success",
    #     "code": 200,
    #     "message": "Data saved successfully!"
    # }
    #
    # Чтобы не растягивать пост, я решил разбить эту тему на
    # несколько частей. Во второй части рассмотрим: преобразование
    # Python-объектов в JSON, настройку сериализации JSON, а также
    # несколько советов по использованию модуля json.
    #
    #
    #
    #
    # https://t.me/c/2383487131/227
    # https://t.me/c/2383487131/227👨‍💻 Гайд: Как работать с JSON в Python. Часть 2
    #
    # В первой части (https://t.me/c/2383487131/221) мы разобрались с чтением и записью JSON-данных. Теперь давайте посмотрим, как преобразовать Python-объекты в JSON, настроить сериализацию и эффективно использовать модуль json.
    #
    # 1️⃣ Преобразование Python-объектов в JSON
    #
    # Чтобы конвертировать Python-объект в JSON-строку,
    # используется функция json.dumps:
    #
    # import json
    #
    # # Python-словарь
    # data = {
    #     "name": "Alice",
    #     "age": 25,
    #     "is_active": True
    # }
    #
    # # Преобразование в JSON-строку
    # json_data = json.dumps(data)
    # print(json_data)  # {"name": "Alice", "age": 25,
    # "is_active": true}
    #
    # ➡️ Типы данных Python, такие как dict, list, str, int, float
    # и bool, автоматически преобразуются в их JSON-аналоги.
    #
    # 2️⃣ Настройка сериализации JSON
    #
    # Если данные содержат нестандартные типы, такие как datetime,
    # то их нужно преобразовать перед сериализацией.
    #
    # Пример:
    #
    # import json
    # from datetime import datetime
    #
    # # Python-данные с датой
    # data = {
    #     "name": "Alice",
    #     "created_at": datetime.now()
    # }
    #
    # # Кастомная функция для обработки объектов
    # def custom_serializer(obj):
    #     if isinstance(obj, datetime):
    #         return obj.isoformat()
    #     raise TypeError("Невозможно сериализовать объект")
    #
    # # Сериализация с кастомной функцией
    # json_data = json.dumps(data, default=custom_serializer,
    # indent=4)
    # print(json_data)
    #
    #  💡 Советы и трюки при работе с JSON
    #
    # 1️⃣ Форматированный вывод JSON
    #
    # Добавьте параметр indent для читабельности:
    #
    # json_data = json.dumps(data, indent=4)
    #
    # 2️⃣ Сортировка ключей
    #
    # Для сортировки ключей используйте sort_keys=True:
    #
    # json_data = json.dumps(data, sort_keys=True)
    #
    # 3️⃣ Декодирование больших чисел
    #
    # Используйте parse_int и parse_float для контроля обработки
    # чисел:
    #
    # json.loads('{"big_number": 12345678901234567890}',
    # parse_int=lambda x: int(x))

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
