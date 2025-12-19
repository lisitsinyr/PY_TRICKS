#------------------------------------------
# f_strings_f_strings11_tricks ():
#------------------------------------------
def f_strings_f_strings11_tricks ():
    """f_strings_f-strings11_tricks"""
#beginfunction
    print ('#-----------------------------')
    print ('#', f_strings_f_strings11_tricks.__name__)
    print ('#-----------------------------')

    #------------------------------------------
    # Плюсы и минусы методов интерполяции строк
    # Как вы уже поняли, f-строки и метод .format() являются полезными методами интерполяции строк. Давайте сравним их.
    #------------------------------------------
    # Функционал	                f-строки	            .format()	    %-форматирование
    # Читаемость	                🟢 Лучше всего	        🟡 ОК	        🔴 Хуже всего
    # Производительность	        🟢 Выше всего	        🟡 Меньше	    🔴 Ниже всего
    # Поддержка выражений	        🟢 Есть	                🟡 Косвенная	🔴 Нет
    # Поддержка многострочных строк	🟢 Есть	                🟢 Есть	        🔴 Нет
    # Простота использования	    🟢 Выше всего	        🟡 Средняя	    🔴 Ниже всего
    # Отладка (оператор =)	        🟢 Есть (Python 3.8+)	🔴 Нет	        🔴 Нет

    #------------------------------------------
    # Когда следует использовать .format(), а не f-строки?
    # Преимущество	Почему стоит использовать .format()?
    #------------------------------------------
    # Поддержка легаси-кода	            Работает в Python 2.7+
    # Гибкий порядок	П               озволяет легко менять местами плейсхолдеры
    # Динамическое форматирование	    Работает, если спецификатор формата динамический
    # Лучшая обработка фигурных скобок	Позволяет обойтись без дополнительного ручного экранирования
    # Работа со словарями	            Проще использовать ключи словарей

    # Сравнение производительности f-строк и .format()
    import timeit
    name = "Alice"
    age = 30
    pi = 3.1415926535
    # Measure f-string performance
    f_string_time = timeit.timeit (
        'f"My name is {name} and I am {age} years old."', globals=globals (),
        number=1000000)
    # Measure .format() performance
    format_time = timeit.timeit (
        '"My name is {} and I am {} years old.".format(name, age)',
        globals=globals (), number=1000000)
    # Measure f-string performance with expressions
    f_string_expr_time = timeit.timeit (
        'f"Pi rounded to 2 decimal places: {pi:.2f}"', globals=globals (),
        number=1000000)
    # Measure .format() performance with expressions
    format_expr_time = timeit.timeit (
        '"Pi rounded to 2 decimal places: {:.2f}".format(pi)',
        globals=globals (), number=1000000)
    # Print results
    print (f"f-string (simple): {f_string_time:.6f} seconds")
    print (f".format() (simple): {format_time:.6f} seconds")
    print (f"f-string (with expression): {f_string_expr_time:.6f} seconds")
    print (f".format() (with expression): {format_expr_time:.6f} seconds")

    #------------------------------------------
    # Лучшие практики для чистой и читабельной интерполяции строк
    #------------------------------------------
    # 1. Для удобочитаемости отдавайте предпочтение f-строкам (Python 3.6+)
    # Recommended
    name = "Alice"
    age = 30
    print (f"My name is {name} and I am {age} years old.")
    # Not Recommended (Less readable)
    print ("My name is {} and I am {} years old.".format (name, age))
    # Avoid using % formatting (Outdated)
    print ("My name is %s and I am %d years old." % (name, age))
    # 2. Используйте именованные плейсхолдеры для ясности.
    # Named placeholders (readable)
    user = {"name": "Alice", "age": 30}
    print (f"My name is {user ['name']} and I am {user ['age']} years old.")
    # Using indexes in .format() (not as readable)
    print ("My name is {0} and I am {1} years old.".format ("Alice", 30))
    # 3. Следите за тем, чтобы многострочные строки были удобочитаемыми.
    name = "Alice"
    age = 30
    message = f"""Hello, {name}!
    We are happy to invite you to our event.
    At {age} years old, you are eligible for the VIP pass.
    Best regards,
    Event Team
    """
    print (message)
    # 4. Для лучшей отладки используйте в логах f-строки.
    value = 42
    # Output: value = 42
    print (f"{value = }")

    #------------------------------------------
    # Как использовать символы Юникода внутри F-Строк?
    #------------------------------------------
    # В документации Python 3.12 есть такой пример:
    # print(f"This is the playlist: {"\N{BLACK HEART SUIT}".join(songs)}")
    #
    # Вывод: This is the playlist: Take me back to
    # Eden♥️Alkaline♥️Ascensionism
    #
    # Но почему "BLACK HEART SUIT" преобразовался в ♥️?
    #
    # Итак, нам необходимо перейти на данный сайт (https://www.htmlsymbols.xyz/),
    # выбрать любой символ, и определить его идентификатор как на скрине выше.
    # F-Строка сама преобразует значение в нужный символ

    #------------------------------------------
    # В Python можно использовать интерполяцию строк (string interpolation), чтобы именовать переменные. Вот примеры:
    #------------------------------------------
    # with open(f'aWord{name}.txt', "w") as f1:
    #  for line in f:
    #  f1.write(line)

    # Вот несколько способов "загнать" variable в имя файла.txt:

    # '{}.txt'.format(variable)
    # '{one}.txt'.format(one=variable)
    # '%s.txt' % variable
    # f'{variable}'
    #
    # Этот трюк поможет при обработке объектов разной длины.


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f_strings_f_strings11_tricks ()
#endif

#endmodule
