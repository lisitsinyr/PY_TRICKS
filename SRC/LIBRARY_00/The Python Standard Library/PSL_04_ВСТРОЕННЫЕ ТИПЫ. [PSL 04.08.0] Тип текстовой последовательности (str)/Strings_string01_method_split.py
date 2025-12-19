#------------------------------------------
# Strings_string01_method_split ():
#------------------------------------------
def Strings_string01_method_split ():
    """Strings_string01_method_split"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string01_method_split.__name__}')
    print (f'#-----------------------------')

    # В этом вам поможет split() с ее позиционным аргументом sep (разделителем):

    txt = "apple#banana#cherry#orange"
    x = txt.split("#")
    print(x)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string01_method_split ()
#endif

#endmodule
