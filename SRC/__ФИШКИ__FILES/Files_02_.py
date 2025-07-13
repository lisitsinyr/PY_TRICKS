#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')
https://t.me/python_easy_ru/810
🤔 Как Python взаимодействует с файлом?

Предоставляет мощные и гибкие инструменты для работы с
файлами. Основные операции включают чтение, запись, создание
и удаление файлов.

🚩Методы

1⃣Открытие файла
Используется функция open(), которая возвращает объект
файла. open() принимает два основных аргумента:
- Имя файла (путь к файлу).
- Режим открытия файла (например, чтение, запись, добавление
и т.д.).
Примеры режимов:
- 'r': Открытие для чтения (по умолчанию).
- 'w': Открытие для записи (содержимое файла удаляется).
- 'a': Открытие для добавления (данные добавляются в конец
файла).
- 'b': Бинарный режим (например, 'rb' или 'wb').
- '+': Открытие для чтения и записи (например, 'r+' или
'w+').
file = open('example.txt', 'r')

2⃣Чтение из файла
Для чтения данных из файла используются методы read(),
readline() и readlines().
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

Пример чтения файла построчно:
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

3⃣Запись в файл
Для записи данных в файл используются методы write() и
writelines().
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

Пример добавления строки в конец файла:
with open('example.txt', 'a') as file:
    file.write('\nAppend this line')

4⃣Закрытие файла
Важно закрывать файл после работы с ним, чтобы освободить
ресурсы. Это можно сделать с помощью метода close(), но
лучше использовать конструкцию with, которая автоматически
закрывает файл:
with open('example.txt', 'r') as file:
    content = file.read()
    # Файл автоматически закроется по завершении блока with

Пример полного цикла работы с файлом
# Открытие файла для записи
with open('example.txt', 'w') as file:
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')

# Открытие файла для добавления
with open('example.txt', 'a') as file:
    file.write('This line is added to the end of the
file.\n')

# Открытие файла для чтения
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

5⃣Работа с бинарными файлами
Для работы с бинарными файлами используется режим 'b'.
Например, чтение и запись изображений или других бинарных
данных
# Чтение бинарного файла
with open('image.png', 'rb') as file:
    data = file.read()

# Запись в бинарный файл
with open('copy_image.png', 'wb') as file:
    file.write(data)

6⃣Исключения и обработка ошибок
Для обработки ошибок при работе с файлами можно использовать
конструкцию try except:
try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
