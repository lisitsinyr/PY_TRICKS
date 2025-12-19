#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/Python_per_month/2910
    # ➡️ Превращение функций в методы класса с помощью
    # types.MethodType
    #
    # types.MethodType — это способ динамического добавления
    # функций в экземпляры класса как методы. Это позволяет
    # создавать методы "на лету" и добавлять их в объекты, что
    # может быть полезно в сложных сценариях, когда структура
    # класса определяется динамически.
    #
    # 🗣️ В этом примере функция external_function добавляется в
    # экземпляр класса MyClass как метод. Это позволяет вызывать
    # её как обычный метод класса, используя атрибуты экземпляра.
    #
    # eee
    # from types import MethodType
    #
    # class MyClass:
    # def __init__(self, value):
    #
    # ——
    # — self.value = value
    # ——
    #
    # def external_function(self, increment):
    # return self.value + increment
    #
    # # Iipespalilaem g¢yHKyno B MeTOg 3K3eMN—NIApPa KNacca
    # instance = MyClass(10)
    # instance.method = MethodType(external_function,
    #
    # instance)
    #
    # print(instance.method(5)) # Bsisog: 15

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
