#------------------------------------------
# f_strings_f_strings01_str ():
#------------------------------------------
def f_strings_f_strings01_str ():
    """f_strings_f_strings01_str"""
#beginfunction
    print ('#-----------------------------')
    print ('#', f_strings_f_strings01_str.__name__)
    print ('#-----------------------------')

    #------------------------------------------
    #
    #------------------------------------------
    vartest_str: str = 'vartest_str'
    print ('default:', vartest_str)
    width = 20
    padding = '_'
    # :<    Left aligns the result (within the available space)
    print ('Left   :', f'{vartest_str:{padding}<{width}}')
    # :>    Right aligns the result (within the available space)
    print ('Right  :', f'{vartest_str:{padding}>{width}}')
    # :^    Center aligns the result (within the available space)
    print ('Center :', f'{vartest_str:{padding}^{width}}')

    #------------------------------------------
    #
    #------------------------------------------
    vartest_str: str = 'vartest_str'
    print ('default:', vartest_str)
    width = 20
    padding = '.'
    print (f'{vartest_str.center (width, padding)}')

    #------------------------------------------
    # Сырые (raw) f-строки
    #------------------------------------------
    name = 'Джон'
    print (f'Его зовут {name!r}')   # 'Джон'
    # unicode
    print (f'Его зовут {name!a}')   # '\u0414\u0436\u043e\u043d'
    # string
    print (f'Его зовут {name!s}')   # Джон

    #------------------------------------------
    # preserves whitespace [сохраняет пробел]
    #------------------------------------------
    foo = 'bar'
    print (f'{ foo = }')            # foo = 'bar'

    #------------------------------------------
    #
    #------------------------------------------
    line = "The mill's closed"
    print(f'{line = }')             #line = "The mill's closed"
    print(f'{line = !r:20}')        #line = "The mill's closed"
    print(f'{line = !a:20}')        #line = "The mill's closed"
    print(f'{line = :20}')          #line = The mill's closed
    print(f'{line = !s:20}')        #line = The mill's closed

    #------------------------------------------
    #
    #------------------------------------------
    name = "Fred"
    print (f'He said his name is {name!s}')
    print (f'He said his name is {name!a}')
    print (f'He said his name is {name!r}')
    print (f'He said his name is {repr (name)}')  # repr() is equivalent to !r

    #------------------------------------------
    #
    #------------------------------------------
    string = "Hi There 😁"
    print (f'{string!a}')
    print (f'{string!r}')
    print (f'{string!s}')

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f_strings_f_strings01_str ()
#endif

#endmodule
