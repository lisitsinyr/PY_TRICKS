#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Исключения в Python 1
    # Исключения в Python
    # Для реализации собственного типа исключения необходимо создать класс,
    # являющийся наследником от одного из классов исключений.
    # class NegValException(Exception):
    # pass
    # try:
    # val = int(input("input positive number: "))
    # if val <0:
    # raise NegValException("Neg val: " + str(val))
    # print(val +10)
    # except NegValException as e:
    # print(e)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
