"""Metaclasses_.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2022-2025
 Author:
     Lisitsin Y.R.
 Project:
     LIBRARY_PY
 Module:
     Metaclasses_.py
 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# Metaclasses_ ():
#------------------------------------------
def Metaclasses_ ():
    """Metaclasses_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Metaclasses_.__name__)
    print ('#-----------------------------')

    # https://t.me/python_practics/934
    # Метаклассы
    #
    # Метаклассы - это классы классов. Они позволяют настраивать
    # поведение создания класса в Python.
    #
    # class SingletonMeta(type):
    # _instances = {}
    #
    # def __call__(cls, *args, **kwargs):
    # if cls not in cls._instances:
    # cls._instances[cls] =
    # super().__call__(*args, **kwargs)
    # return cls._instances[cls]
    #
    # class Singleton(metaclass=SingletonMeta) :
    # pass
    #
    # obj1 = Singleton( )
    # obj2 = Singleton( )
    # print(obj1 is obj2) # Output: True

#endfunction

#------------------------------------------
# main ():
#------------------------------------------
def main ():
    """main"""
#beginfunction
    Metaclasses_ ()
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
