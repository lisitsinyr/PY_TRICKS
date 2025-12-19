#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Link: https://t.me/pytstart/286
    #
    # Дата: 2025-06-15 16:18:27+00:00
    #
    # Title: PytStart | Программирование на Python
    #
    # 🧩** Structural Pattern Matching в Python 3.10+ — наконец-то
    # нормальный match-case**
    #
    # Ты ждал switch в Python?
    # Python 3.10 привёз не просто switch, а настоящий мощный
    # match — с распаковкой, шаблонами, guard’ами и даже классами.
    #
    # 👍** Базовое использование match-case**
    # ```
    # def handle_command(cmd):
    #     match cmd:
    #         case "start":
    #             print("Запуск...")
    #         case "stop":
    #             print("Остановка.")
    #         case _:
    #             print("Неизвестная команда.")```
    # _ — это как default в switch. Срабатывает, если ничего не
    # подошло.
    #
    # 👍** Распаковка списков**
    # ```
    # def handle_coords(point):
    #     match point:
    #         case [0, 0]:
    #             print("Начало координат")
    #         case [x, 0]:
    #             print(f"На оси X: x = {x}")
    #         case [0, y]:
    #             print(f"На оси Y: y = {y}")
    #         case [x, y]:
    #             print(f"Где-то в пространстве: ({x}, {y})")```
    # Можно писать как шаблоны — работает магия распаковки прямо в
    # кейсах.
    #
    # 👍 Распаковка словарей
    # ```
    # def describe_user(user):
    #     match user:
    #         case {"name": name, "age": age}:
    #             print(f"{name}, возраст {age}")
    #         case {"name": name}:
    #             print(f"Имя: {name}, возраст неизвестен")```
    # Словари матчатся по ключам.
    #
    #
    # 👍 match-классы с **match_args**
    # ```
    # class Point:
    #     __match_args__ = ("x", "y")
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #
    # def process(obj):
    #     match obj:
    #         case Point(0, 0):
    #             print("Центр")
    #         case Point(x, y):
    #             print(f"Точка: ({x}, {y})")```
    # Так можно матчить прямо по объектам.
    #
    # 👍 Guard — фильтрация в кейсе
    # ```
    # def check_number(n):
    #     match n:
    #         case x if x > 0:
    #             print("Положительное")
    #         case x if x < 0:
    #             print("Отрицательное")
    #         case _:
    #             print("Ноль")```
    # Можно фильтровать значения прямо в кейсе.
    #
    # 👍 Матч с распаковкой и остатком
    # ```
    # def analyze(data):
    #     match data:
    #         case [first, *middle, last]:
    #             print(f"Начало: {first}, конец: {last},
    # середина: {middle}")```
    # *middle — как в списках: «всё, что посередине».
    #
    # 👍 Комбинации: tuple + шаблон + guard
    # ```
    # def react(event):
    #     match event:
    #         case ("click", x, y) if x > 0 and y > 0:
    #             print("Клик по области")
    #         case ("keypress", key):
    #             print(f"Нажата клавиша {key}")
    #         case _:
    #             print("Неизвестное событие")```
    # Можно матчить по типу события, распаковывать и фильтровать —
    # мощь.
    #
    # 🗣️** Запомни:** Structural Pattern Matching — это не просто
    # switch, это способ писать выразительный, компактный и
    # читабельный код.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
