#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/c/2383487131/324
    # 📱 Фишка: inspect.signature — анализ аргументов функции во
    # время выполнения
    #
    # Можно динамически получать информацию о параметрах функции,
    # не заглядывая в её код. Это полезно для логирования,
    # автогенерации документации и работы с API.
    #
    # import inspect
    #
    # def example_function(a: int, b: str = "hello", *args,
    # **kwargs):
    #     pass
    #
    # sig = inspect.signature(example_function)
    #
    # for name, param in sig.parameters.items():
    #     print(f"{name}: {param.annotation} = {param.default}")
    #
    # 📌 Как это работает?
    #
    # 🟢 inspect.signature() извлекает параметры функции, включая
    # их имена, типы и значения по умолчанию.
    # 🟢 Полезно для создания обёрток, валидации аргументов и
    # анализа стороннего кода.
    # 🟢 Позволяет работать с любыми функциями, включая методы
    # классов и лямбда-функции.
    #
    # def dynamic_func(**kwargs):
    #     print("Переданные аргументы:", kwargs)
    #
    # sig = inspect.signature(dynamic_func)
    # print(sig)  # **kwargs

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
