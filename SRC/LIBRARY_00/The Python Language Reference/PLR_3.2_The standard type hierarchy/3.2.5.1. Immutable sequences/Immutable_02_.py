#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Link: https://t.me/pytstart/284
    #
    # Дата: 2025-06-15 13:02:37+00:00
    #
    # Title: PytStart | Программирование на Python
    #
    # 🔗** Immutable структуры в Python**: `frozendict`,
    # `namedtuple`, `frozen dataclass`
    #
    # Хочешь, чтобы данные нельзя было случайно затереть?
    # В проде часто нужны **неизменяемые структуры** — особенно в
    # конфигурациях, кэше, многопоточке.

    # ✅ 1. `namedtuple` **— старый, но быстрый**
    from collections import namedtuple
    User = namedtuple("User", ["id", "name"])
    u = User(1, "Neo")
    print(u.name)     # Neo
    # u.name = "Morpheus"  # ❌ AttributeError```
    # 👉 Создаёт лёгкий класс с фиксированными полями, нельзя
    # мутировать.

    #  ✅ 2. `@dataclass(frozen=True)` **— удобно и читаемо**
    from dataclasses import dataclass
    @dataclass(frozen=True)
    class User:
        id: int
        name: str
    u = User(2, "Trinity")
    print(u.name)     # Trinity
    # u.name = "Smith"  # ❌ FrozenInstanceError```
    # 👌 Плюс — автогенерация `__init__`, `__repr__`, сравнение и
    # хеш.

    #  ✅ 3. `frozendict` **— словарь, который не меняется**
    from types import MappingProxyType
    config = MappingProxyType({
        "host": "localhost",
        "port": 8080
    })
    print(config["host"])      # localhost
    # config["host"] = "127.0.0.1"  # ❌ TypeError```
    # Это нативная альтернатива `frozendict`, без внешних либ.
    # Используется, когда нужен **read-only dict**.

    #  ✅** 4. Хардкорный** `frozendict` **через стороннюю либу**
    from frozendict import frozendict  # pip install frozendict
    settings = frozendict(api="v1", retries=3)
    print(settings["api"])     # v1
    # settings["api"] = "v2"   # ❌ TypeError```
    # Здесь dict ведёт себя как set — хешируем и защищён.

    # ✅ **5. Где это реально юзается:**
    # ✅ Кэш: ключи не должны меняться
    cache_key = frozendict(user="admin", page=1)
    # ✅ Конфиги и константы
    @dataclass(frozen=True)
    class DBConf:
        host: str
        port: int
    # ✅ Многопоточность — безопасная передача```

    # 🗣️** Запомни: **`frozen=True`, `namedtuple`,
    # `MappingProxyType` и `frozendict` — всё это про **чистые,
    # безопасные, защищённые структуры**.Если ты не хочешь, чтобы
    # кто-то случайно изменил важные данные — **используй их без
    # сомнений**.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
