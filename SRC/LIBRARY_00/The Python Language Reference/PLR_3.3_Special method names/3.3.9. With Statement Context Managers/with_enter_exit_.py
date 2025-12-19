#------------------------------------------
# with_enter_exit_ ():
#------------------------------------------
def with_enter_exit_ ():
    """with_enter_exit_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', with_enter_exit_.__name__)
    print ('#-----------------------------')

    # https://t.me/python_easy_ru/1021
    # 🤔 Расскажи о методах enter и exit ?
    #
    # Методы __enter__ и exit являются частью протокола менеджера
    # контекста. Они позволяют объектам определять поведение в
    # контексте оператора with. Эти методы обеспечивают безопасное
    # и автоматическое управление ресурсами, такими как файлы,
    # сетевые соединения и другие объекты, которые требуют явного
    # открытия и закрытия.
    #
    # 🚩Протокол менеджера контекста
    #
    # 🟠__enter__(self)
    # Выполняется в начале блока with и возвращает объект, который
    # будет присвоен переменной, указанной после as.
    # 🟠__exit__(self, exc_type, exc_value, traceback)
    # Выполняется в конце блока with, независимо от того,
    # произошло исключение или нет. Он используется для очистки и
    # освобождения ресурсов.
    #
    # class ManagedResource:
    #     def __enter__(self):
    #         print("Entering the context")
    #         return self
    #
    #     def __exit__(self, exc_type, exc_value, traceback):
    #         print("Exiting the context")
    #         if exc_type:
    #             print(f"Exception type: {exc_type}")
    #             print(f"Exception value: {exc_value}")
    #             print(f"Traceback: {traceback}")
    #         return True  # True указывает на то, что исключение
    # было обработано
    #
    # # Использование
    # with ManagedResource() as resource:
    #     print("Inside the context")
    #
    # print("Outside the context")
    #
    # Пример управления файлом с использованием менеджера
    # контекста
    # class FileManager:
    #     def __init__(self, filename, mode):
    #         self.filename = filename
    #         self.mode = mode
    #
    #     def __enter__(self):
    #         self.file = open(self.filename, self.mode)
    #         return self.file
    #
    #     def __exit__(self, exc_type, exc_value, traceback):
    #         self.file.close()
    #         if exc_type:
    #             print(f"Exception type: {exc_type}")
    #             print(f"Exception value: {exc_value}")
    #             print(f"Traceback: {traceback}")
    #         return True
    #
    # # Использование
    # with FileManager("example.txt", "w") as f:
    #     f.write("Hello, World!")
    #
    # print("File operation completed")


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    with_enter_exit_ ()
#endif

#endmodule
