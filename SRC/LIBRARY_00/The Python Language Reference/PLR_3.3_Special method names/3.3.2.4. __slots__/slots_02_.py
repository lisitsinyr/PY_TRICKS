#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Link: https://t.me/pytstart/292
    #
    # Дата: 2025-06-17 13:08:31+00:00
    #
    # Title: PytStart | Программирование на Python
    #
    # 🪄 `__slots__` **в Python — ускоряем и экономим на классах**
    #
    # Если ты создаёшь **кучу объектов**, каждый по умолчанию
    # несёт с собой **`__dict__`**, который ест память.
    # А теперь представь: у тебя 100 000 таких объектов. Зачем
    # лишний мусор?
    #
    # 🔧 Без `__slots__`: обычный класс
    # ```class User:
    #     def __init__(self, name, email):
    #         self.name = name
    #         self.email = email
    #
    # users = [User(f"user{i}", f"u{i}@mail.com") for i in
    # range(100_000)]```
    # Каждый объект несёт `__dict__`. Замерим:
    # ```import sys
    # u = User("test", "t@mail.com")
    # print(sys.getsizeof(u))          # 56
    # print(sys.getsizeof(u.__dict__))  # 232```
    # 📦 Итог: \~300 байт на одного → \~30 МБ на 100К объектов.
    #
    #  ⚡️ С `__slots__`
    # ```class User:
    #     __slots__ = ['name', 'email']
    #
    #     def __init__(self, name, email):
    #         self.name = name
    #         self.email = email
    #
    # users = [User(f"user{i}", f"u{i}@mail.com") for i in
    # range(100_000)]```
    #
    # ```u = User("test", "t@mail.com")
    # print(sys.getsizeof(u))  # 48```
    #
    # 💥 **Почти в 5 раз меньше памяти. И никакого** `__dict__`:
    # ```print(hasattr(u, '__dict__'))  # False```
    #
    #  🚫 **Слоты = строгая структура**
    # ```u.age = 42
    # # ❌ AttributeError: 'User' object has no attribute 'age'```
    #
    #
    # 🗣️** Запомни**:`__slots__` — это жёстко, экономно и
    # быстро.Ты получаешь фиксированную структуру, меньше памяти и
    # ускорение доступа к атрибутам.
    # Не юзай их везде — только там, где реально важно.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
