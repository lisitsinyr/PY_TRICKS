#------------------------------------------
# Escapes_01_ ():
#------------------------------------------
def Escapes_01_ ():
    """Escapes_01_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Escapes_01_.__name__)
    print ('#-----------------------------')

    width = 60
    padding = '_'

    # +---------------------------+-----------------------------------+---------+
    # Escape Sequence           
    # "\"<newline>              
    Title = 'Backslash and newline ignored'
    print (f'{Title:{padding}<{width}}')
    print ("test \
    ")

    # "\\" - Backslash ("\")
    Title = 'Backslash ("\\")'
    print (f'{Title:{padding}<{width}}')
    print ("\\")

    # "\'" - Single quote ("'")
    Title = 'Single quote ("\'")'
    print (f'{Title:{padding}<{width}}')
    print ("\'")

    # "\"" - Double quote (""")
    Title = 'Double quote (""")'
    print (f'{Title:{padding}<{width}}')
    print ("\"")

    # "\a" - ASCII Bell (BEL)
    Title = 'ASCII Bell (BEL)'
    print (f'{Title:{padding}<{width}}')
    print ("1\a2")

    # "\b" - ASCII Backspace (BS)
    Title = 'ASCII Backspace (BS)'
    print (f'{Title:{padding}<{width}}')
    print ("1\b2")
    
    # "\f" - ASCII Formfeed (FF)
    Title = 'ASCII Formfeed (FF)'
    print (f'{Title:{padding}<{width}}')
    print ("1\f2")
    
    # "\n" - ASCII Linefeed (LF)
    Title = '"ASCII Linefeed (LF)"'
    print (f'{Title:{padding}<{width}}')
    print ("1\n2")
    
    # "\r" - ASCII Carriage Return (CR)
    Title = 'ASCII Carriage Return (CR)'
    print (f'{Title:{padding}<{width}}')
    print ("1\r2")
    
    # "\t" - ASCII Horizontal Tab (TAB)
    Title = 'ASCII Horizontal Tab (TAB)'
    print (f'{Title:{padding}<{width}}')
    print ("1\t2")
    
    # "\v" - ASCII Vertical Tab (VT)
    Title = 'ASCII Vertical Tab (VT)'
    print (f'{Title:{padding}<{width}}')
    print ("\v")
    
    # "\*ooo*" - Character with octal value *ooo*
    Title = 'Character with octal value *ooo*'
    print (f'{Title:{padding}<{width}}')
    print ("\60")
    
    # "\x*hh*" - Character with hex value *hh*
    Title = 'Character with hex value *hh*'
    print (f'{Title:{padding}<{width}}')
    print ("\x30")
    
    # +---------------------------+-----------------------------------+---------+
    # Escape sequences only recognized in string literals are:
    # +---------------------------+-----------------------------------+---------+
    # | Escape Sequence           | Meaning                           | Notes   |
    # | "\N{*name*}"              | Character named *name* in the     | (5)     |
    # |                           | Unicode database                  |         |
    #print ("\N{*name*}")

    # | "\u*xxxx*"                | Character with 16-bit hex value   | (6)     |
    # |                           | *xxxx*                            |         |
    #print ("\u*xxxx*")

    # | "\U*xxxxxxxx*"            | Character with 32-bit hex value   | (7)     |
    # |                           | *xxxxxxxx*                        |         |
    #print ("\U*xxxxxxxx*")
    # +---------------------------+-----------------------------------+---------+

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Escapes_01_ ()
#endif

#endmodule
