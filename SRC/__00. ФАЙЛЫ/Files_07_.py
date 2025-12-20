#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')
https://t.me/python_easy_ru/1093
🤔 Какие есть виды файловых объектов?

В Python существует несколько типов файловых объектов,
которые используются для работы с различными типами данных.
Рассмотрим основные виды файловых объектов и их особенности.

🟠Текстовые файлы (`TextIOWrapper`)
Это самый распространённый тип файловых объектов. Такие
файлы используются для работы с текстовыми данными и
поддерживают строковые операции.
   with open("example.txt", "w", encoding="utf-8") as file:
       file.write("Привет, мир!")  # Записываем текст в файл

   with open("example.txt", "r", encoding="utf-8") as file:
       content = file.read()  # Читаем текст из файла
       print(content)

🟠Бинарные файлы (`BufferedReader`, `BufferedWriter`)
Эти файлы используются для работы с двоичными данными
(изображениями, видео, аудиофайлами и т. д.).
   with open("image.jpg", "rb") as file:
       binary_data = file.read()  # Читаем файл в бинарном
режиме
       print(binary_data[:10])  # Выведем первые 10 байтов

   with open("copy.jpg", "wb") as file:
       file.write(binary_data)  # Записываем данные в новый
файл

🟠Файлы ввода-вывода в памяти (`io.StringIO`, `io.BytesIO`)
Эти объекты представляют собой файловые буферы, которые
хранят данные в оперативной памяти, а не на диске.
   from io import StringIO

   file = StringIO()
   file.write("Привет, мир!")  # Запись данных в буфер
   file.seek(0)  # Перемещаем указатель в начало
   print(file.read())  # Читаем данные из буфера

Пример работы с BytesIO:
   from io import BytesIO

   file = BytesIO()
   file.write(b"Binary data")  # Запись бинарных данных
   file.seek(0)
   print(file.read())  # Чтение данных

🟠Файловые объекты на основе сокетов, пайпов и других
источников
Python позволяет работать с файловыми объектами, полученными
из нестандартных источников, например, сокетов или каналов
связи (pipes).
   import socket

   s = socket.socket()
   s.connect(("example.com", 80))
   s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
   response = s.makefile("r", encoding="utf-8")  # Создание
файлового объекта
   print(response.readline())  # Читаем первую строку HTTP-
ответа
   s.close()


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
