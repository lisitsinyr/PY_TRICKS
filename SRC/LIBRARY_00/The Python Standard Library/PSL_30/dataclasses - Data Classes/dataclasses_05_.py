#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/pytstart/158
    # 👩‍💻 Python dataclasses: убираем бойлерплейт красиво
    #
    # 📋 `@dataclass` — удобный способ определить классы без ручной
    # возни с `__init__`, `__repr__`, `__eq__`, и т.д.
    #
    #  🤯 До появления dataclasses
    #
    # Вот как выглядел простой класс раньше:
    #
    #
    # class Book:
    #     def __init__(self, title, pages):
    #         self.title = title
    #         self.pages = pages
    #
    #     def __repr__(self):
    #         return f"Book(title={self.title},
    # pages={self.pages})"
    #
    # Скучно, многословно и легко ошибиться.
    #
    #  ✔️ Теперь с `@dataclass`
    #
    # from dataclasses import dataclass
    #
    # @dataclass
    # class Book:
    #     title: str
    #     pages: int
    #
    #
    # Python сам сгенерирует:
    #
    # - `__init__`
    # - `__repr__`
    # - `__eq__`
    # - `__hash__` (если надо)
    # - `__lt__`, `__gt__`, если задать `order=True`
    #
    #  🔧 Доп. фичи
    #
    # - Значения по умолчанию:
    #
    # @dataclass
    # class User:
    #     name: str
    #     is_admin: bool = False
    #
    # - Поля без участия в сравнении/выводе:
    #
    # from dataclasses import field
    #
    # @dataclass
    # class Session:
    #     token: str = field(repr=False, compare=False)
    #
    # - Иммутабельность:
    #
    # @dataclass(frozen=True)
    # class Point:
    #     x: int
    #     y: int
    #
    # - `__post_init__` — для логики после __init__:
    #
    # @dataclass
    # class Product:
    #     name: str
    #     price: float
    #
    #     def __post_init__(self):
    #         if self.price < 0:
    #             raise ValueError("Price cannot be negative")
    #
    #
    # 🗣 @dataclass избавляет от шаблонного кода, улучшает
    # читаемость и идеально подходит для приложений, где важны
    # чистые структуры данных: от ML до веб-сервисов.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
