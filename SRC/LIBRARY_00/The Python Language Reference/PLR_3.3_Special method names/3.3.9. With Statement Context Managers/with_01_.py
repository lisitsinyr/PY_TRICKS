#------------------------------------------
# with_01_ ():
#------------------------------------------
def with_01_ ():
    """with_01_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', with_01_.__name__)
    print ('#-----------------------------')

    # https://t.me/Python_libr/1645
    # 📌 Context Manager
    #
    # Это мощный инструмент для управления ресурсами: файлами,
    # которые нужно закрывать, соединениями, блокировками. Если
    # что-то нужно сделать после работы с файлом, лучше всего
    # использовать with.
    #
    # Оператор вызывает __enter__ у объекта, выполняет
    # первоначальные функции, а по окончанию работы — exit, где
    # менеджер может освободить ресурсы, закрыть файл или
    # соединение.
    #
    #
    # import psycopg2
    #
    # class DatabaseConnection:
    # def _init_(self, host, database, user, password):
    # self.host = host
    # self.database = database
    # self.user = user
    # self.password = password
    #
    # def _enter_(self):
    # self.conn = psycopg2.connect(
    # host=self.host,
    # database=self.database,
    # user=self.user,
    # password=self.password
    # )
    #
    # return self.conn
    #
    # _exit_(self, type, value, traceback):
    # self.conn.close()
    #
    # with DatabaseConnection("localhost", "mydatabase", "user", "password") as conn:
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM mytable”)
    # rows = cur.fetchall()


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    with_01_ ()
#endif

#endmodule
