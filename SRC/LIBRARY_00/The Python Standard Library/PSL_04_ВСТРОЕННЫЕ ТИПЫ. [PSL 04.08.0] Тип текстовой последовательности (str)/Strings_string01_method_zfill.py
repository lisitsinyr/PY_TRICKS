#------------------------------------------
# Strings_string01_method_zfill ():
#------------------------------------------
def Strings_string01_method_zfill ():
    """Strings_string01_method_zfill"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method_zfill.__name__}')
    print (f'#-----------------------------')

    # Метод zfill() в Python применяется к строкам и используется для добавления
    # нулей в начале строки до определенной длины.
    # Этот метод полезен, когда необходимо получить строку определенной длины,
    # даже если исходная строка короче.
    print ("42".zfill (5))
    # 00042
    print ("-42".zfill (5))
    # -0042

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method_zfill ()
#endif

#endmodule
