#------------------------------------------
# bytes_literals_01_ ():
#------------------------------------------
def bytes_literals_01_ ():
    """bytes_literals_01_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', bytes_literals_01_.__name__)
    print ('#-----------------------------')

    # bytesliteral   ::= bytesprefix(shortbytes | longbytes)
    # bytesprefix    ::= "b" | "B" | "br" | "Br" | "bR" | "BR" | "rb" | "rB" | "Rb" | "RB"
    # shortbytes     ::= "'" shortbytesitem* "'" | '"' shortbytesitem* '"'
    # longbytes      ::= "'''" longbytesitem* "'''" | '"""' longbytesitem* '"""'
    # shortbytesitem ::= shortbyteschar | bytesescapeseq
    # longbytesitem  ::= longbyteschar | bytesescapeseq
    # shortbyteschar ::= <any ASCII character except "\" or newline or the quote>
    # longbyteschar  ::= <any ASCII character except "\">
    # bytesescapeseq ::= "\" <any ASCII character>

    print ('------------------------------------------------------')
    print ('bytesprefix "b" | "B" | "br" | "Br" | "bR" | "BR" | "rb" | "rB" | "Rb" | "RB"')
    print ('------------------------------------------------------')
    b = b'test'
    print (b)
    b = B'test'
    print (b)
    b = br'test'
    print (b)
    b = BR'test'
    print (b)

    print ('------------------------------------------------------')
    print ('shortbytes')
    print ('------------------------------------------------------')
    b = b'test'
    print (b)
    b = b"test"
    print (b)

    print ('------------------------------------------------------')
    print ('longbytes')
    print ('------------------------------------------------------')
    b = b'''test'''
    print (b)
    b = b"""test"""
    print (b)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    bytes_literals_01_ ()
#endif

#endmodule
