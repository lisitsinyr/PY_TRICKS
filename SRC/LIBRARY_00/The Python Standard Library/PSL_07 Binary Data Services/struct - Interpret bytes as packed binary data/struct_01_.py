#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/Python_per_month/2489
    # struct.Struct()
    #
    # Модуль struct позволяет преобразовывать между Python-
    # значениями и C-структурами, представленными как объекты
    # bytes. Компактные форматные строки описывают предполагаемые
    # преобразования в/из Python-значений.
    #
    # Синтаксис:
    # struct.Struct(format_string)
    #
    # Аргументы:
    # format_string — строка формата, описывающая структуру.
    #
    # eee
    # ~ _ import struct
    # # Co3qaémM CTpykTypy ¢ QBYMaA a2neMeHTaMu: OaviToM u“ LeENbIM 4YucCNOM
    # struct_format = "bh"
    #
    # struct = struct.Struct(struct_format)
    #
    # # CoxpaHsem faHHble B CTpyKType
    # struct_data = struct.pack(struct_format, 1, 255)
    #
    # # MN3BNeKaeM AaHHble U3 CTPYKTYpbl
    # byte_value, integer_value = struct.unpack(struct_format, struct_data)
    #
    # print(byte_value, integer_value)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
