#------------------------------------------
# Decorators_01_ ():
#------------------------------------------
def Decorators_01_ ():
    """Decorators_01_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Decorators_01_.__name__)
    print ('#-----------------------------')

    # https://uproger.com/metaprogrammirovanie-na-grani-magii-metaklassy-dekoratory-i-dinamicheskie-dsl/

    # 3. Декораторы: магические обёртки для функций и классов
    # 3.1 Основы декораторов
    # Декораторы — это функции, которые принимают другую функцию или класс и возвращают модифицированную версию оригинала. Они позволяют добавить дополнительное поведение (например, логирование, кэширование, проверку прав доступа) без изменения исходного кода функции.
    #
    # 3.2 Пример декоратора для логирования вызовов функций
    # Рассмотрим простой декоратор, который выводит сообщение до и после вызова функции:
    #
    # pythonКопироватьРедактироватьimport functools
    #
    # def log_calls(func):
    #     @functools.wraps(func)
    #     def wrapper(*args, **kwargs):
    #         print(f"Вызов {func.__name__} с аргументами: {args}, {kwargs}")
    #         result = func(*args, **kwargs)
    #         print(f"{func.__name__} вернула: {result}")
    #         return result
    #     return wrapper
    #
    # @log_calls
    # def add(a, b):
    #     return a + b
    #
    # print(add(2, 3))
    # Объяснение:
    # Декоратор log_calls принимает функцию func и возвращает функцию-обёртку wrapper, которая добавляет логирование до и после вызова оригинальной функции. Использование functools.wraps помогает сохранить метаданные оригинальной функции.
    #
    # 3.3 Декораторы для классов
    # Декораторы могут применяться и к классам. Например, можно создать декоратор, который регистрирует все методы класса или изменяет их поведение:
    #
    # pythonКопироватьРедактироватьdef uppercase_methods(cls):
    #     for attr_name, attr_value in cls.__dict__.items():
    #         if callable(attr_value) and not attr_name.startswith("__"):
    #             # Оборачиваем метод в декоратор, который преобразует строковый результат в верхний регистр
    #             original_method = attr_value
    #             def new_method(self, *args, _original_method=original_method, **kwargs):
    #                 result = _original_method(self, *args, **kwargs)
    #                 if isinstance(result, str):
    #                     return result.upper()
    #                 return result
    #             setattr(cls, attr_name, new_method)
    #     return cls
    #
    # @uppercase_methods
    # class Greeter:
    #     def greet(self, name):
    #         return f"Hello, {name}!"
    #
    # greeter = Greeter()
    # print(greeter.greet("world"))
    # Объяснение:
    # Декоратор uppercase_methods перебирает все атрибуты класса, находит методы (исключая специальные методы) и заменяет их на версии, которые преобразуют возвращаемую строку в верхний регистр. Это позволяет изменять поведение всех методов класса единовременно.




    # 4. Динамические DSL: создание доменно-специфичных языков
    # DSL (Domain-Specific Language) — это язык, ориентированный на определённую область применения. С помощью метапрограммирования можно создавать DSL, которые будут читабельными и интуитивно понятными для специалистов конкретной области.
    #
    # 4.1 Пример DSL для описания схемы данных
    # Представим, что нам необходимо создать DSL для описания структуры модели данных, аналогичный тому, как работают ORM (например, SQLAlchemy или Django ORM). Мы можем использовать метаклассы и декораторы для регистрации полей модели и создания декларативного синтаксиса.
    #
    # pythonКопироватьРедактировать# Поля модели
    # class Field:
    #     def __init__(self, field_type):
    #         self.field_type = field_type
    #
    # class IntegerField(Field):
    #     def __init__(self):
    #         super().__init__('integer')
    #
    # class StringField(Field):
    #     def __init__(self, max_length=255):
    #         super().__init__('string')
    #         self.max_length = max_length
    #
    # # Метакласс для моделей
    # class ModelMeta(type):
    #     def __new__(mcs, name, bases, attrs):
    #         # Собираем все поля, определённые в классе
    #         fields = {}
    #         for key, value in list(attrs.items()):
    #             if isinstance(value, Field):
    #                 fields[key] = value
    #                 # Удаляем поля из атрибутов, чтобы не мешали обычным атрибутам класса
    #                 attrs.pop(key)
    #         attrs['_fields'] = fields
    #         cls = super().__new__(mcs, name, bases, attrs)
    #         return cls
    #
    # # Базовый класс модели
    # class Model(metaclass=ModelMeta):
    #     def __init__(self, **kwargs):
    #         for field_name in self._fields:
    #             setattr(self, field_name, kwargs.get(field_name))
    #
    #     def __repr__(self):
    #         field_values = ', '.join(f"{name}={getattr(self, name)!r}" for name in self._fields)
    #         return f"<{self.__class__.__name__} {field_values}>"
    #
    # # Определяем модель с использованием DSL
    # class User(Model):
    #     id = IntegerField()
    #     name = StringField(max_length=100)
    #     email = StringField(max_length=100)
    #
    # # Использование модели
    # user = User(id=1, name="Alice", email="alice@example.com")
    # print(user)
    # print("Поля модели:", User._fields)
    # Объяснение:
    #
    # Определение полей: Мы создаём базовый класс Field и его наследников (IntegerField, StringField). Это позволяет описывать типы данных.
    # Метакласс ModelMeta: При создании нового класса модели (наследника Model) метакласс собирает все атрибуты, являющиеся экземплярами Field, и сохраняет их в специальном атрибуте _fields. Таким образом, модель становится декларативной.
    # Базовый класс Model: Реализует конструктор, который принимает значения для полей, и метод __repr__, чтобы удобно выводить объект.
    # Такой подход позволяет создавать лёгкие DSL для описания моделей, абстрагируя детали реализации.
    #
    # 4.2 Динамическое изменение DSL с помощью декораторов
    # Декораторы могут расширить возможности DSL. Например, можно создать декоратор для добавления валидации к полям модели:
    #
    # pythonКопироватьРедактироватьdef validate_fields(validation_func):
    #     def decorator(cls):
    #         original_init = cls.__init__
    #         def new_init(self, *args, **kwargs):
    #             original_init(self, *args, **kwargs)
    #             for field_name, field in self._fields.items():
    #                 value = getattr(self, field_name)
    #                 if not validation_func(field, value):
    #                     raise ValueError(f"Неверное значение для поля '{field_name}': {value}")
    #         cls.__init__ = new_init
    #         return cls
    #     return decorator
    #
    # # Функция валидации: например, проверяем, что строковые поля не пустые
    # def simple_validator(field, value):
    #     if field.field_type == 'string' and not value:
    #         return False
    #     return True
    #
    # @validate_fields(simple_validator)
    # class Product(Model):
    #     id = IntegerField()
    #     name = StringField(max_length=50)
    #     description = StringField(max_length=200)
    #
    # # Попытка создать некорректную модель
    # try:
    #     product = Product(id=10, name="", description="Описание товара")
    # except ValueError as e:
    #     print("Ошибка валидации:", e)
    # Объяснение:
    # Декоратор validate_fields принимает функцию валидации и оборачивает конструктор класса, добавляя проверку для каждого поля. Если значение не проходит валидацию, выбрасывается исключение. Такой подход позволяет легко расширять DSL дополнительной логикой.
    #
    # 5. Заключение
    # Метапрограммирование в Python открывает широкие возможности для создания гибких, декларативных и масштабируемых систем.
    #
    # Метаклассы позволяют вмешиваться в процесс создания классов, автоматически регистрируя или модифицируя их.
    # Декораторы служат для обёртывания функций и классов, добавляя к ним новое поведение без изменения исходного кода.
    # Динамические DSL дают возможность создавать компактный и выразительный синтаксис для описания предметной области, что особенно полезно при разработке ORM, фреймворков и систем конфигурации.
    # Использование этих техник требует глубокого понимания внутренних механизмов Python, но взамен они дают мощные инструменты для повышения гибкости и расширяемости вашего кода. Надеюсь, данная статья поможет вам освоить азы магии метапрограммирования и применять её для решения сложных задач.
    #
    # Это лишь базовый обзор возможностей метапрограммирования в Python. Экспериментируйте, комбинируйте декораторы и метаклассы, и вы сможете создавать настоящие доменно-специфичные языки, адаптированные под нужды вашего проекта.

    

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Decorators_01_ ()
#endif

#endmodule
