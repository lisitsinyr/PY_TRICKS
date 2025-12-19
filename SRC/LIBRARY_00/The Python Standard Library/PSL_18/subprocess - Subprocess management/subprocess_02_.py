#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/python2day/6284
    # 🚀 Работа с системными командами в Python: модуль subprocess
    #
    # subprocess — мощный модуль Python, который позволяет
    # запускать внешние команды и программы, а также
    # взаимодействовать с их вводом и выводом. Отличный инструмент
    # для автоматизации системных задач!
    #
    # Основные возможности
    # ✅ Запуск shell-команд (ls, dir, ping и др.)
    # ✅ Получение вывода команды прямо в Python.
    # ✅ Запуск внешних программ и скриптов.
    # ✅ Проверка доступности серверов через ping.
    # ✅ Автоматизация системного администрирования.
    #
    # Примеры использования
    #
    # 📌 Вывод списка файлов (Linux/macOS)
    #
    # import subprocess
    # result = subprocess.run(['ls', '-l'], capture_output=True,
    # text=True)
    # print(result.stdout)
    #
    # 📌 Вывод списка процессов (Windows)
    #
    # import subprocess
    # result = subprocess.run(['tasklist'], shell=True,
    # capture_output=True, text=True)
    # print(result.stdout)
    #
    # 📌 Проверка доступности сервера (Linux)
    #
    # import subprocess
    # server = "google.com"
    # result = subprocess.run(["ping", "-c", "4", server],
    # capture_output=True, text=True)
    #
    # if result.returncode == 0:
    #     print("Сервер доступен")
    #     print(result.stdout)
    # else:
    #     print("Сервер недоступен")
    #     print(result.stderr)
    #
    # Ключевые функции:
    # ➡️ subprocess.run() – Запуск команды и ожидание завершения.
    # ➡️ subprocess.Popen() – Запуск команды с возможностью
    # взаимодействия.
    # ➡️ subprocess.check_call() – Проверка выполнения команды (с
    # исключением в случае ошибки).
    # ➡️ subprocess.check_output() – Запуск команды с возвратом
    # результата.
    #
    # subprocess — это мост между Python и системой, позволяющий
    # автоматизировать администрирование, анализ данных и работу с
    # внешними программами.
    #
    # 📂 Используйте, тестируйте, автоматизируйте!

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
