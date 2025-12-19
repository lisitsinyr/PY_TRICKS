#------------------------------------------
# f_strings_f_strings05_debugging ():
#------------------------------------------
def f_strings_f_strings05_debugging ():
    """f_strings_f_strings05_debugging"""
#beginfunction
    print ('#-----------------------------')
    print ('#', f_strings_f_strings05_debugging.__name__)
    print ('#-----------------------------')

    #------------------------------------------
    #
    #------------------------------------------
    x = 10
    y = 20
    # print(f'x = {x}, y = {y}')
    print(f'{x=},{y=}')
    #------------------------------------------
    # math operations
    print(f'{x*y=}')
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f_strings_f_strings05_debugging ()
#endif

#endmodule
