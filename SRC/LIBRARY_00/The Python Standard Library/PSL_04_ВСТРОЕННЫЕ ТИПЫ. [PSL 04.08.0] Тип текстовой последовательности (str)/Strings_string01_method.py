#------------------------------------------
# Strings_string01_method ():
#------------------------------------------
def Strings_string01_method ():
    """Strings_string01_method"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method.__name__}')
    print (f'#-----------------------------')

    width = 60
    padding = '_'

    # Базовые операции

    Title = 'Конкатенация (сложение)'
    print (f'{Title:{padding}<{width}}')
    S1 = 'spam'
    S2 = 'eggs'
    print(S1 + S2)
    # 'spameggs'
    # String Concatenation
    # To concatenate, or combine, two strings you can use the + operator.
    # Example
    # Merge variable a with variable b into variable c:
    # a = "Hello"
    # b = "World"
    # c = a + b
    # print(c)
    # Example
    # To add a space between them, add a " ":
    # a = "Hello"
    # b = "World"
    # c = a + " " + b
    # print(c)

    


    Title = 'Дублирование строки'
    print (f'{Title:{padding}<{width}}')
    print('spam' * 3)
    # spamspamspam

    Title = 'Длина строки (функция len)'
    print (f'{Title:{padding}<{width}}')
    len('spam')    # 4

    Title = 'Доступ по индексу'
    S = 'spam'
    print(S[0])        # 's'
    print(S[2])        # 'a'
    print(S[-2])       # 'a'
    # Как видно из примера, в Python возможен и доступ по отрицательному индексу, при этом отсчет идет от конца строки.

    Title = 'Извлечение среза'
    print (f'{Title:{padding}<{width}}')
    # Оператор извлечения среза: [X:Y]. X – начало среза, а Y – окончание;
    # символ с номером Y в срез не входит. По умолчанию первый индекс равен 0, а второй - длине строки.
    s = 'spameggs'
    s[3:5]      # 'me'
    s[2:-2]     # 'ameg'
    s[:6]       # 'spameg'
    s[1:]       # 'pameggs'
    s[:]        # 'spameggs'
    # Кроме того, можно задать шаг, с которым нужно извлекать срез.
    s[::-1]     # 'sggemaps'
    s[3:5:-1]   # ''
    s[2::2]     # 'aeg'

    Title = 'Другие функции и методы строк'
    print (f'{Title:{padding}<{width}}')
    # При вызове методов необходимо помнить, что строки в Python относятся к категории неизменяемых последовательностей, то есть все функции и методы могут лишь создавать новую строку.
    s = 'spam'
    s[1] = 'b'
    # Traceback (most recent call last):
    #   File "", line 1, in
    #     s[1] = 'b'
    # TypeError: 'str' object does not support item assignment
    s = s[0] + 'b' + s[2:]
    s  # 'sbam'
    # Поэтому все строковые методы возвращают новую строку, которую потом следует присвоить переменной.

    Title = 'Функции и методы строк'
    print (f'{Title:{padding}<{width}}')

    Title = 'Литералы строк'
    print (f'{Title:{padding}<{width}}')
    S = 'str';
    S = "str";
    S = '''str''';
    S = """str"""

    Title = 'Экранированные последовательности'
    print (f'{Title:{padding}<{width}}')
    S = "s\np\ta\nbbb"

    Title = 'Неформатированные строки (подавляют экранирование)'
    print (f'{Title:{padding}<{width}}')
    S = r"C:\temp\new"

    Title = 'Строка байтов'
    print (f'{Title:{padding}<{width}}')
    S = b"byte"

    Title = 'Конкатенация (сложение строк)'
    print (f'{Title:{padding}<{width}}')
    S1 = 'spam'
    S2 = 'eggs'
    print(S1 + S2)
    # 'spameggs'

    Title = 'Повторение строки'
    print (f'{Title:{padding}<{width}}')
    # S1 * 3
    print('S1' * 3)

    Title = 'Обращение по индексу'
    print (f'{Title:{padding}<{width}}')
    # S[i]

    Title = 'Извлечение среза'
    print (f'{Title:{padding}<{width}}')
    # S[i:j:step]

    Title = 'Длина строки'
    print (f'{Title:{padding}<{width}}')
    # len(S)

    Title = 'Поиск подстроки в строке. Возвращает номер первого вхождения или -1'
    print (f'{Title:{padding}<{width}}')
    print('hello WORLD'.find('OR'))
    # S.find(str, [start],[end])

    Title = 'Поиск подстроки в строке. Возвращает номер последнего вхождения или -1'
    print (f'{Title:{padding}<{width}}')
    # S.rfind(str, [start],[end])

    Title = 'Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError'
    print (f'{Title:{padding}<{width}}')
    # S.index(str, [start],[end])
    print('31/01/2022'.index(''))

    Title = 'Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError'
    print (f'{Title:{padding}<{width}}')
    # S.rindex(str, [start],[end])

    Title = 'Замена шаблона на замену. maxcount ограничивает количество замен'
    print (f'{Title:{padding}<{width}}')
    # S.replace(шаблон, замена[, maxcount])
    print('31/01/2022'.replace('/','-'))

    Title = 'Разбиение строки по разделителю'
    print (f'{Title:{padding}<{width}}')
    # S.split(символ)
    print('abc123'.split('c'))

    Title = 'Состоит ли строка из цифр'
    print (f'{Title:{padding}<{width}}')
    # S.isdigit()
    print('12345'.isnumeric())

    Title = 'Состоит ли строка из букв'
    print (f'{Title:{padding}<{width}}')
    # S.isalpha()

    Title = 'Состоит ли строка из цифр или букв'
    print (f'{Title:{padding}<{width}}')
    # S.isalnum()
    print('A12345'.isalnum())

    Title = 'Состоит ли строка из символов в нижнем регистре'
    print (f'{Title:{padding}<{width}}')
    # S.islower()
    print('hello WORLD'.islower())

    Title = 'Состоит ли строка из символов в верхнем регистре'
    print (f'{Title:{padding}<{width}}')
    # S.isupper()
    print('HELLO WORLD'.isupper())

    Title = '''
        Состоит ли строка из неотображаемых символов (
        пробел, 
        символ перевода страницы ('\f'), 
        новая строка ('\n'), 
        перевод каретки ('\r'), 
        горизонтальная табуляция ('\t')
        вертикальная табуляция ('\v'))
        '''
    print (f'{Title:{padding}<{width}}')
    # S.isspace()

    Title = 'Начинаются ли слова в строке с заглавной буквы'
    print (f'{Title:{padding}<{width}}')
    # S.istitle()

    Title = 'Преобразование строки к верхнему регистру'
    print (f'{Title:{padding}<{width}}')
    # S.upper()
    print('hello WORLD'.upper())

    Title = 'Преобразование строки к нижнему регистру'
    print (f'{Title:{padding}<{width}}')
    # S.lower()
    print('hello WORLD'.lower())

    Title = 'Начинается ли строка S с шаблона str'
    print (f'{Title:{padding}<{width}}')
    # S.startswith(str)

    Title = 'Заканчивается ли строка S шаблоном str'
    print (f'{Title:{padding}<{width}}')
    # S.endswith(str)

    Title = 'Сборка строки из списка с разделителем S'
    print (f'{Title:{padding}<{width}}')
    # S.join(список)

    Title = 'Символ в его код ASCII'
    print (f'{Title:{padding}<{width}}')
    # ord(символ)

    Title = 'Код ASCII в символ'
    print (f'{Title:{padding}<{width}}')
    # chr(число)

    Title = 'Переводит первый символ строки в верхний регистр, а все остальные в нижний'
    print (f'{Title:{padding}<{width}}')
    # S.capitalize()
    print('hello WORLD'.capitalize())

    Title = 'Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)'
    print (f'{Title:{padding}<{width}}')
    # S.center(width, [fill])
    print('Python'.center(10, '*'))

    Title = 'Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)'
    print (f'{Title:{padding}<{width}}')
    # S.count(str, [start],[end])
    print('HELLO WORLD'.count('O'))

    Title = 'Возвращает копию строки, в которой все символы табуляции заменяются одним или несколькими пробелами, в зависимости от текущего столбца. Если TabSize не указан, размер табуляции полагается равным 8 пробелам'
    print (f'{Title:{padding}<{width}}')
    # S.expandtabs([tabsize])

    Title = 'Удаление пробельных символов в начале строки'
    print (f'{Title:{padding}<{width}}')
    # S.lstrip([chars])

    Title = 'Удаление пробельных символов в конце строки'
    print (f'{Title:{padding}<{width}}')
    # S.rstrip([chars])

    Title = 'Удаление пробельных символов в начале и в конце строки'
    print (f'{Title:{padding}<{width}}')
    # S.strip([chars])

    Title = 'Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки'
    print (f'{Title:{padding}<{width}}')
    # S.partition(шаблон)

    Title = 'Возвращает кортеж, содержащий часть перед последним шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий две пустых строки, а затем саму строку'
    print (f'{Title:{padding}<{width}}')
    # S.rpartition(sep)

    Title = 'Переводит символы нижнего регистра в верхний, а верхнего – в нижний'
    print (f'{Title:{padding}<{width}}')
    # S.swapcase()

    Title = 'Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний'
    print (f'{Title:{padding}<{width}}')
    # S.title()

    Title = 'Делает длину строки не меньшей width, по необходимости заполняя первые символы нулями'
    print (f'{Title:{padding}<{width}}')
    # S.zfill(width)

    Title = 'Делает длину строки не меньшей width, по необходимости заполняя последние символы символом fillchar'
    print (f'{Title:{padding}<{width}}')
    # S.ljust(width, fillchar=" ")

    Title = 'Делает длину строки не меньшей width, по необходимости заполняя первые символы символом fillchar'
    print (f'{Title:{padding}<{width}}')
    # S.rjust(width, fillchar=" ")

    Title = 'Форматирование строки'
    print (f'{Title:{padding}<{width}}')
    # S.format(*args, **kwargs)
    Title = '    Использование метода .format()'
    # Как и f-строки, метод .format() позволяет вставлять в строку переменные и выражения. Базовый синтаксис метода .format() выглядит следующим образом:
    name = 'Mark'
    output_string = 'My name is {}.'.format(name)
    print(output_string)

    Title = '    Позиционные аргументы'
    print (f'{Title:{padding}<{width}}')
    name = 'Mark'
    age = 7
    # The placeholders are filled in order of the arguments
    output_string = 'My name is {} and I am {} years old.'.format(name, age)
    print(output_string)

    Title = '    Индексированные и именованные плейсхолдеры'
    print (f'{Title:{padding}<{width}}')
    name = 'Mark'
    age = 7
    # Print age twice
    output_string = 'My name is {} and I am {} years old. My twin brother is also {} years old.'.format(name, age, age)
    print(output_string)
    # Здесь мы дважды использовали значение переменной age. Включение одной и той же переменной несколько раз в таком случае выглядит неуклюже и ухудшает читаемость. Можно ли повторно использовать переменную в строке, отформатированной методом .format(), не повторяя ее? Да: с помощью так называемых индексированных плейсхолдеров.
    name = 'Mark'
    age = 7
    # Use indexed placeholders
    output_string = 'My name is {0} and I am {1} years old. My twin brother is also {1} years old.'.format(name, age)
    print(output_string)
    # В качестве альтернативы позиционной индексации можно также использовать именованные аргументы, когда каждому аргументу присваивается имя.
    print('My name is {name} and I am {age} years old.'.format(name='Mark', age=7))

    Title = '    Использование оператора %'
    print (f'{Title:{padding}<{width}}')
    # Последний метод интерполяции строк — оператор %. Он работает аналогично команде printf() в C. Его использование устарело и категорически не рекомендуется. Здесь он упомянут, потому что вы можете встретить его в старых кодовых базах.
    # Основной формат оператора % таков: "форматируемая строка" % значения. Форматируемая строка содержит плейсхолдеры (для строк — %s), которые заменяются значениями. Например, в следующем примере выводится «Hello, Mark».
    # 'Hello, %s' % 'Mark'
    # Спецификатор    Значение    Пример
    # %s  Строка  "Hello %s" % "Alice" → "Hello Alice"
    # %d  Целое десятичное число  "Age: %d" % 25 → "Age: 25"
    # %f  Число с плавающей точкой (по умолчанию 6 знаков после точки)    "Pi: %f" % 3.14159 → "Pi: 3.141590"
    # %.nf    Число с плавающей точкой (n знаков после точки) "%.2f" % 3.14159 → "3.14"
    # %x  Шестнадцатеричное число (в нижнем регистре) "%x" % 255 → "ff"
    # %X  Шестнадцатеричное число (в верхнем регистре)    "%X" % 255 → "FF"
    # %o  Восьмеричное число  "%o" % 255 → "377"
    # Многострочные строки также можно создавать с помощью метода .format().
    name = 'Mark'
    profession = 'Astronaut'
    age = 7
    # This is a multiline string with .format()
    bio = """
    Name: {}
    Profession: {}
    Age: {}
    """.format(name, profession, age)
    print(bio)

    Title = '    Генерация многострочных электронных писем или сообщений'
    print (f'{Title:{padding}<{width}}')
    name = "Alice"
    event = "Annual Tech Conference"
    date = "March 15, 2025"
    email = """Dear {name},
    We are pleased to invite you to the {event} taking place on {date}.
    We hope you can join us for an exciting experience.
    Best regards, 
    The Event Team""".format(name=name, event=event, date=date)
    print(email)

    Title = '    Форматирование с помощью метода .format() аналогично:'
    print (f'{Title:{padding}<{width}}')
    from math import pi
    print('Pi rounded to 2 decimal places: {:.2f}'.format(pi))
    print('Pi rounded to 4 decimal places: {:.4f}'.format(pi))
    print('Pi rounded to 0 decimal places: {:.0f}'.format(pi))



#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method ()
#endif

#endmodule
