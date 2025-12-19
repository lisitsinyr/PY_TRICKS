#------------------------------------------
# Keywords_11_Variable_Handling_Keywords ():
#------------------------------------------
def Keywords_11_Variable_Handling_Keywords ():
    """Keywords_11_Variable_Handling_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_11_Variable_Handling_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Variable Handling Keywords: del,global,nonlocal')
    print ('------------------------------------------------------')
    # Three Python keywords are used to work with variables. The del keyword is more commonly used than the global and nonlocal keywords. But it’s still helpful to know and understand all three keywords so you can identify when and how to use them.

    print ('------------------------------------------------------')
    print ('The del Keyword')
    print ('------------------------------------------------------')
    # The del keyword is used in Python to unset a variable or name. While you can use it on variable names, it’s more commonly used to remove indexes from a list or dictionary. To unset a variable, use del followed by the variable you want to unset:
    #
    # del <variable>
    # Let’s assume you want to clean up a dictionary that you got from an API response by throwing out keys you know you won’t use. You can do so with the del keyword:
    #
    # >>> del response["headers"]
    # >>> del response["errors"]
    # This will remove the "headers" and "errors" keys from the dictionary response.
    #
    # To learn more about the del keyword, check out the tutorial Python’s del: Remove References From Scopes and Containers.

    print ('------------------------------------------------------')
    print ('The global Keyword')
    print ('------------------------------------------------------')
    # If you need to modify a variable that isn’t defined in a function but is defined in the global scope, then you’ll need to use the global keyword. This works by specifying in the function which variables need to be pulled into the function from the global scope:
    #
    # global <variable>
    # A basic example is incrementing a global variable with a function call. You can do that with the global keyword:
    #
    x = 0
    def inc():
        global x
        x += 1
    
    inc()
    # >>> x
    # 1
    # >>> inc()
    # >>> x
    # 2
    # This is generally not considered good practice, but it does have its uses. To learn much more about the global keyword, check out Python Scope & the LEGB Rule: Resolving Names in Your Code.

    print ('------------------------------------------------------')
    print ('The nonlocal Keyword')
    print ('------------------------------------------------------')
    # The nonlocal keyword is similar to global in that it allows you to modify variables from a different scope. With global, the scope you’re pulling from is the global scope. With nonlocal, the scope you’re pulling from is the parent scope. The syntax is similar to global:
    #
    # nonlocal <variable>
    # This keyword isn’t used very often, but it can be handy at times. For a deeper understanding of scoping and the nonlocal keyword, refer to Python Scope & the LEGB Rule: Resolving Names in Your Code.
    
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_11_Variable_Handling_Keywords ()
#endif

#endmodule
