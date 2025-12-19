#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/c/2383487131/445
    # 😡 Гайд по работе с базами данных SQLite в Python
    #
    # SQLite — отличный выбор для локального хранения данных, и
    # sqlite3 в Python делает его использование простым и удобным.
    # Давайте разберём основные операции с базами данных, начиная
    # с создания, вставки данных, обновления и удаления.
    #
    # 1️⃣ Создание и подключение к базе данных:
    #
    # import sqlite3
    #
    # # Подключение к базе данных (создаётся новая, если не
    # существует)
    # conn = sqlite3.connect('example.db')
    # cursor = conn.cursor()
    #
    # 2️⃣ Создание таблицы:
    #
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS users (
    #     id INTEGER PRIMARY KEY,
    #     name TEXT,
    #     age INTEGER
    # )
    # ''')
    #
    # 3️⃣ Вставка данных:
    #
    # cursor.execute('INSERT INTO users (name, age) VALUES (?,
    # ?)', ('Alice', 30))
    # conn.commit()  # Сохраняем изменения
    #
    # 4️⃣ Получение данных:
    #
    # cursor.execute('SELECT * FROM users')
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    #
    # 5️⃣ Обновление данных:
    #
    # cursor.execute('UPDATE users SET age = ? WHERE name = ?',
    # (31, 'Alice'))
    # conn.commit()
    #
    # 6️⃣ Удаление данных:
    #
    # cursor.execute('DELETE FROM users WHERE name = ?',
    # ('Alice',))
    # conn.commit()
    #
    # 📌 Советы
    #
    # 🟢 Используйте параметризованные запросы (? или :) для защиты
    # от SQL-инъекций.
    # 🟢 Закрывайте соединение с базой после завершения работы:
    # conn.close().
    # ❗️ SQLite подходит для небольших проектов, тестирования или
    # хранения локальных данных.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
