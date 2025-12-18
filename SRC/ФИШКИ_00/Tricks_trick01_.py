from pathlib import Path

#------------------------------------------
# Tricks_trick01 ():
#------------------------------------------
def Tricks_trick01 ():
    """Tricks_trick01"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Tricks_trick01.__name__}')
    print (f'#-----------------------------')

    width = 60
    padding = '_'

    # 30 трюков на Python с описанием преимущества
    # https://habr.com/ru/companies/datafeel/articles/870920/

    Title = '1. Списковые включения (List Comprehensions)'
    print (f'{Title:{padding}<{width}}')
    # print (f'{Title:{"."}<{60}}')
    squares = [x**2 for x in range(10)]
    print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    # Преимущества: Код становится более компактным и легко воспринимаемым, улучшая читаемость и производительность благодаря встроенной оптимизации.
    #
    Title = '2. Генераторы'
    print (f'{Title:{padding}<{width}}')
    def generate_numbers(n):
        for i in range(n):
            yield i * 2

    gen = generate_numbers(5)
    print(list(gen))  # [0, 2, 4, 6, 8]
    # Преимущества: Генераторы экономят память, создавая значения по мере необходимости, что особенно полезно для больших наборов данных.
    #
    Title = '3. Функция enumerate()'
    print (f'{Title:{padding}<{width}}')
    # fruits = ['apple', 'banana', 'cherry']
    # for index, fruit in enumerate(fruits):
    #     print(index, fruit)
    # # 0 apple
    # # 1 banana
    # # 2 cherry
    # Преимущества: Упрощает получение индекса и значения одновременно без необходимости управления счетчиком.
    #
    Title = '4. Функция zip()'
    print (f'{Title:{padding}<{width}}')
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    combined = list(zip(names, ages))
    print(combined)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
    # Преимущества: Позволяет удобно объединять несколько списков в кортежи, упрощая работу с парами значений.
    #
    # 5. Использование *args и **kwargs
    #
    def example_function(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)

    example_function(1, 2, 3, name="Alice", age=25)
    # args: (1, 2, 3)
    # kwargs: {'name': 'Alice', 'age': 25}
    # Преимущества: Обеспечивает гибкость в передаче произвольного количества аргументов и именованных параметров в функции.
    #
    # 6. Словари с пониманием (Dictionary Comprehensions)
    #
    squares_dict = {x: x**2 for x in range(5)}
    print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    # Преимущества: Позволяет создавать словари более лаконично и читаемо, чем с использованием циклов.
    #
    # 7. Функция map()
    #
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # [1, 4, 9, 16]
    # Преимущества: Упрощает применение функции ко всем элементам списка без необходимости использовать циклы.
    #
    # 8. Функция filter()
    #
    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # [2, 4]
    # Преимущества: Позволяет легко фильтровать элементы списка по заданному условию.
    #
    # 9. Использование set() для удаления дубликатов
    #
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = set(numbers)
    print(unique_numbers)  # {1, 2, 3, 4, 5}
    # Преимущества: Быстро удаляет дубликаты, обеспечивая уникальность элементов.
    #
    # 10. Функция sorted()
    #
    unsorted_list = [5, 2, 3, 1, 4]
    sorted_list = sorted(unsorted_list)
    print(sorted_list)  # [1, 2, 3, 4, 5]
    # Преимущества: Упрощает сортировку списков, предоставляя возможность сортировать по умолчанию или по заданным критериям.
    #
    # 11. Использование defaultdict из модуля collections
    #
    from collections import defaultdict

    dd = defaultdict(int)
    dd['apple'] += 1
    dd['banana'] += 2
    print(dd)  # defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
    # Преимущества: Позволяет автоматизировать создание ключей со значениями по умолчанию, что упрощает управление словарями.
    #
    # 12. Использование Counter из модуля collections
    #
    from collections import Counter

    fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    count = Counter(fruits)
    print(count)  # Counter({'banana': 3, 'apple': 2, 'orange': 1})
    # Преимущества: Удобно подсчитывает количество вхождений элементов, обеспечивая простой анализ частоты.
    #
    # 13. Использование itertools для создания итераторов
    #
    import itertools

    count = itertools.count(start=5, step=2)
    print(next(count))  # 5
    print(next(count))  # 7
    # Преимущества: Позволяет создавать бесконечные итераторы, которые можно использовать для генерации последовательностей.
    #
    # 14. Использование with для управления ресурсами
    #
    with open('example.txt', 'w') as f:
        f.write('Hello, World!')
    # Файл автоматически закрывается после выхода из блока with
    # Преимущества: Обеспечивает автоматическое управление ресурсами, предотвращая утечки памяти и открытые файлы.
    #
    # 15. Функция any() и all()
    #
    numbers = [1, 2, 3, 4]
    print(any(x > 3 for x in numbers))  # True
    print(all(x > 0 for x in numbers))  # True
    # Преимущества: Упрощает проверку условий для коллекций, позволяя быстро оценивать логические выражения.
    #
    # 16. Использование lambda для создания анонимных функций
    #
    add = lambda x, y: x + y
    print(add(5, 3))  # 8
    # Преимущества: Позволяет создавать краткие функции на месте, что удобно для небольших операций.
    #
    # 17. Использование try и except для обработки исключений
    #
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Деление на ноль!")
    # Преимущества: Обеспечивает безопасное управление ошибками, предотвращая аварийное завершение программы.
    #
    # 18. Использование f-строк для форматирования строк
    #
    name = "Alice"
    age = 30
    print(f"{name} is {age} years old.")  # Alice is 30 years old.
    # Преимущества: Позволяет легко и удобно форматировать строки, улучшая читаемость кода.
    #
    # 19. Использование re для работы с регулярными выражениями
    #
    import re

    text = "The rain in Spain"
    match = re.search(r'\bS\w+', text)
    print(match.group())  # Spain
    # Преимущества: Упрощает поиск и манипуляцию строками с использованием мощных регулярных выражений.
    #
    # 20. Использование json для работы с JSON данными
    #
    import json

    data = {'name': 'Alice', 'age': 30}
    json_data = json.dumps(data)
    print(json_data)  # {"name": "Alice", "age": 30}
    # Преимущества: Позволяет легко сериализовать и десериализовать данные в формате JSON, что полезно для работы с API.
    #
    # 21. Использование datetime для работы с датами и временем
    #
    from datetime import datetime

    now = datetime.now()
    print(now)  # Текущая дата и время
    # Преимущества: Упрощает работу с датами и временем, предоставляя доступ к различным атрибутам и методам.
    #
    # 22. Использование os и sys для работы с операционной системой
    #
    import os

    current_directory = os.getcwd()
    print(current_directory)  # Текущий рабочий каталог
    # Преимущества: Позволяет взаимодействовать с операционной системой, получая информацию о файловой системе и среде выполнения.
    #
    # 23. Использование pickle для сериализации объектов
    #
    import pickle

    data = {'name': 'Alice', 'age': 30}
    with open('data.pkl', 'wb') as f:
        pickle.dump(data, f)

    with open('data.pkl', 'rb') as f:
        loaded_data = pickle.load(f)
    print(loaded_data)  # {'name': 'Alice', 'age': 30}
    # Преимущества: Упрощает процесс сериализации и десериализации объектов, что полезно для сохранения состояния программы.
    #
    # 24. Использование @staticmethod и @classmethod
    #
    class MyClass:
        @staticmethod
        def static_method():
            return "This is a static method."

        @classmethod
        def class_method(cls):
            return f"This is a class method of {cls.__name__}."

    print(MyClass.static_method())  # This is a static method.
    print(MyClass.class_method())    # This is a class method of MyClass.
    # Преимущества: Позволяет организовывать код и разделять методы, которые работают с экземплярами и классами.
    #
    # 25. Использование property() для создания свойств
    #
    class Person:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

    person = Person("Alice")
    print(person.name)  # Alice
    # Преимущества: Позволяет создавать свойства с контролем доступа, улучшая инкапсуляцию.
    #
    # 26. Использование assert для отладки
    #
    x = 5
    assert x > 0, "x должно быть положительным"  # Не выбрасывает исключение
    # Преимущества: Упрощает отладку, позволяя добавлять проверки условий в коде.
    #
    # 27. Использование timeit для измерения времени выполнения кода
    #
    import timeit

    execution_time = timeit.timeit('sum(range(100))', number=10000)
    print(execution_time)  # Время выполнения
    # Преимущества: Позволяет точно измерять производительность кода, помогая в оптимизации.
    #
    # 28. Использование functools.lru_cache для кэширования результатов
    #
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    print(fibonacci(10))  # 55
    # Преимущества: Ускоряет выполнение рекурсивных функций за счет кэширования результатов, что особенно полезно для вычислений с повторяющимися вызовами.
    #
    # 29. Использование contextlib для создания контекстных менеджеров
    #
    from contextlib import contextmanager

    @contextmanager
    def my_context():
        print("Entering the context")
        yield
        print("Exiting the context")

    with my_context():
        print("Inside the context")
    # Entering the context
    # Inside the context
    # Exiting the context
    # Преимущества: Позволяет создавать пользовательские контекстные менеджеры, улучшая управление ресурсами.
    #
    # 30. Использование numpy и pandas для работы с данными
    #
    import numpy as np
    import pandas as pd

    # Пример с numpy
    array = np.array([1, 2, 3, 4])
    print(array * 2)  # [2 4 6 8]

    # Пример с pandas
    data = {'Name': ['Alice', 'Bob'], 'Age': [30, 25]}
    df = pd.DataFrame(data)
    print(df)
    #    Name  Age
    # 0  Alice   30
    # 1    Bob   25
    # Преимущества: Обеспечивает мощные инструменты для анализа данных и работы с массивами, упрощая манипуляции с большими объемами данных. Про pandas и numpy можно часами хитрости расписывать. Полезно знать хитрость про типы. Очень мощные инструменты!

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Tricks_trick01 ()
#endif

#endmodule
