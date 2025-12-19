#------------------------------------------
# Keywords_02_Value_Keywords ():
#------------------------------------------
def Keywords_02_Value_Keywords ():
    """Keywords_02_Value_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_02_Value_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Value Keywords: True,False,None')
    print ('------------------------------------------------------')
    # There are three Python keywords that are used as values. These values are singleton values that can be used over and over again and always reference the exact same object. You’ll most likely see and use these values a lot.
    # There are a few terms used in the sections below that may be new to you. They’re defined here, and you should be aware of their meaning before proceeding:
    # Truthiness refers to the Boolean evaluation of a value. The truthiness of a value indicates whether the value is truthy or falsy.
    # Truthy means any value that evaluates to true in the Boolean context. To determine if a value is truthy, pass it as the argument to bool(). If it returns True, then the value is truthy. Examples of truthy values are non-empty strings, any numbers that aren’t 0, non-empty lists, and many more.
    # Falsy means any value that evaluates to false in the Boolean context. To determine if a value is falsy, pass it as the argument to bool(). If it returns False, then the value is falsy. Examples of falsy values are "", 0, [], {}, and set().
    # For more on these terms and concepts, check out Operators and Expressions in Python.

    print ('------------------------------------------------------')
    print ('The True and False Keywords')
    print ('------------------------------------------------------')
    # The True keyword is used as the Boolean true value in Python code.
    # The Python keyword False is similar to the True keyword,
    # but with the opposite Boolean value of false. In other programming languages,
    # you’ll see these keywords written in lowercase (true and false),
    # but in Python they’re always capitalized.
    # The Python keywords True and False can be assigned to variables and compared directly:
    x = True
    print  (x is True)
    # True
    y = False
    print  (y is False)
    # True
    # Most values in Python will evaluate to True when passed to bool().
    # There are only a few values in Python that will evaluate to False when passed to bool():
    # 0, "", [], and {} to name a few. Passing a value to bool() indicates the value’s truthiness,
    # or the equivalent Boolean value. You can compare a value’s truthiness
    # to True or False by passing the value to bool():
    x = "this is a truthy value"
    print  (x is True)
    # False
    print  (bool(x) is True)
    # True
    y = ""  # This is falsy
    print  (y is False)
    # False
    print  (bool(y) is False)
    # True
    # Notice that comparing a truthy value directly to True or False using is doesn’t work. You should compare a value to True or False directly only if you want to know whether it’s actually the values True or False.
    # When writing conditional statements that are based on the truthiness of a value, you should not compare directly to True or False. You can rely on Python to do the truthiness check in conditionals for you:
    x = "this is a truthy value"
    if x is True:  # Don't do this
         print("x is True")
    if x:  # Do this
         print("x is truthy")
    # x is truthy
    # In Python, you generally don’t need to convert values to be explicitly True or False. Python will implicitly determine the truthiness of the value for you.
    # To learn more about the True and False keywords in Python, check out the tutorial Python Booleans: Use Truth Values in Your Code.

    print ('------------------------------------------------------')
    print ('The None Keyword')
    print ('------------------------------------------------------')
    # The Python keyword None represents no value. In other programming languages, None is represented as null, nil, none, undef, or undefined.
    # None is also the default value returned by a function if it doesn’t have a return statement:
    def func():
         print("hello")
    x = func()
    # hello
    print(x)
    # None
    # To go more in depth on this very important and useful Python keyword, check out Null in Python: Understanding Python’s NoneType Object.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_02_Value_Keywords ()
#endif

#endmodule
