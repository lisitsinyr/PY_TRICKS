#------------------------------------------
# Keywords_09_Exception-Handling_Keywords ():
#------------------------------------------
def Keywords_09_Exception_Handling_Keywords ():
    """Keywords_09_Exception-Handling_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_09_Exception_Handling_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('xception-Handling Keywords: try,except,raise,finally,else,assert')
    print ('------------------------------------------------------')
    # One of the most common aspects of any Python program is the raising and catching of exceptions. Because this is such a fundamental aspect of all Python code, there are several Python keywords available to help make this part of your code clear and concise.
    #
    # The sections below go over these Python keywords and their basic usage. For a more in-depth tutorial on these keywords, check out Python Exceptions: An Introduction.

    print ('------------------------------------------------------')
    print ('The try Keyword')
    print ('------------------------------------------------------')
    # Any exception-handling block begins with Python’s try keyword. This is the same in most other programming languages that have exception handling.
    #
    # The code inside the try block is code that might raise an exception. Several other Python keywords are associated with try and are used to define what should be done if different exceptions are raised. These keywords are except, else, and finally:
    #
    # try:
    #     <statements>
    # <except|else|finally>:
    #     <statements>
    # A try block isn’t valid unless it has at least one of the other Python keywords used for exception handling as part of the overall try statement.
    #
    # If you wanted to calculate and return the miles per gallon of gas (MPG) given the miles driven and the gallons of gas used, then you could write a function like the following:
    #
    # def miles_per_gallon(miles, gallons):
    #     return miles / gallons
    # The first problem you might see is that your code could raise a ZeroDivisionError if the gallons parameter is passed in as 0. The try keyword allows you to modify the code above to handle that situation appropriately:
    #
    # def miles_per_gallon(miles, gallons):
    #     try:
    #         mpg = miles / gallons
    #     except ZeroDivisionError:
    #         mpg = None
    #     return mpg
    # Now if gallons = 0, then miles_per_gallon() won’t raise an exception and will return None instead. This might be better, or you might decide that you want to raise a different type of exception or handle this situation differently. You’ll see an expanded version of this example below to illustrate the other keywords used for exception handling.
    
    print ('------------------------------------------------------')
    print ('The except Keyword')
    print ('------------------------------------------------------')
    # Python’s except keyword is used with try to define what to do when specific exceptions are raised. You can have one or more except blocks with a single try. The basic usage looks like this:
    #
    # try:
    #     <statements>
    # except <exception>:
    #     <statements>
    # Taking the miles_per_gallon() example from before, you could also do something specific in the event that someone passes types that won’t work with the / operator. Having defined miles_per_gallon() in a previous example, now try to call it with strings instead of numbers:
    #
    # >>> miles_per_gallon("lots", "many")
    # Traceback (most recent call last):
    #   ...
    # TypeError: unsupported operand type(s) for /: 'str' and 'str'
    # You could revise miles_per_gallon() and use multiple except blocks to handle this situation, too:
    #
    def miles_per_gallon(miles, gallons):
        try:
            mpg = miles / gallons
        except ZeroDivisionError:
            mpg = None
        except TypeError as exc:
            print("you need to provide numbers")
            raise exc
        return mpg
    # Here, you modify miles_per_gallon() to raise the TypeError exception only after you’ve printed a helpful reminder to the screen.
    # Note: Since Python 3.11, you can also use except* to filter errors in exception groups. See Python 3.11 Preview: Task and Exception Groups to learn more.
    # Notice that the except keyword can also be used in conjunction with the as keyword. This has the same effect as the other uses of as, giving the raised exception an alias so you can work with it in the except block.
    # Even though it’s syntactically allowed, try not to use except statements as implicit catchalls. It’s better practice to always explicitly catch something, even if it’s just Exception:
    try:
        1 / 0
    except:  # Never do this
        pass
    
    try:
        1 / 0
    except Exception:  # This is better
        pass
    
    try:
        1 / 0
    except ZeroDivisionError:  # This is best
        pass
    # If you really do want to catch a broad range of exceptions, then specify the parent Exception. This is more explicitly a catchall, and it won’t also catch exceptions you probably don’t want to catch, like RuntimeError or KeyboardInterrupt.

    print ('------------------------------------------------------')
    print ('The raise Keyword')
    print ('------------------------------------------------------')
    # The raise keyword raises an exception. If you find you need to raise an exception, then you can use raise followed by the exception to be raised:
    #
    # raise <exception>
    # You used raise previously in the miles_per_gallon() example. When you catch the TypeError, you re-raise the exception after printing a message to the screen.
    #
    # For more on raise, check out Python’s raise: Effectively Raising Exceptions in Your Code.

    print ('------------------------------------------------------')
    # The finally Keyword
    print ('------------------------------------------------------')
    # Python’s finally keyword is helpful for specifying code that should be run no matter what happens in the try, except, or else blocks. To use finally, use it as part of a try block and specify the statements that should be run no matter what:
    #
    # try:
    #     <statements>
    # finally:
    #     <statements>
    # Using the example from before, it might be helpful to specify that, no matter what happens, you want to know what arguments the function was called with. You could modify miles_per_gallon() to include a finally block that does just that:
    #
    def miles_per_gallon(miles, gallons):
        try:
            mpg = miles / gallons
        except ZeroDivisionError:
            mpg = None
        except TypeError as exc:
            print("you need to provide numbers")
            raise exc
        finally:
            print(f"miles_per_gallon({miles}, {gallons})")
        return mpg
    # Now, no matter how miles_per_gallon() is called or what the result is, you print the arguments supplied by the user:
    #
    # >>> miles_per_gallon(10, 1)
    # miles_per_gallon(10, 1)
    # 10.0
    #
    # >>> miles_per_gallon("lots", "many")
    # you need to provide numbers
    # miles_per_gallon(lots, many)
    # Traceback (most recent call last):
    #   ...
    # TypeError: unsupported operand type(s) for /: 'str' and 'str'
    # As you can see, the finally keyword can be a very useful part of your exception-handling code.
    
    print ('------------------------------------------------------')
    print ('The else Keyword Used With try and except')
    print ('------------------------------------------------------')
    # You’ve learned that the else keyword can be used with both the if keyword and loops in Python, but it has one more use. It can be combined with the try and except Python keywords. You can use else in this way only if you also use at least one except block:
    #
    # try:
    #     <statements>
    # except <exception>:
    #     <statements>
    # else:
    #     <statements>
    # In this context, the code in the else block is executed only if no exception is raised in the try block. In other words, if the try block executes all the code successfully, then the else block code will be executed.
    #
    # In the miles_per_gallon() example, imagine you want to make sure that the mpg result is always returned as a float no matter what number combination is passed in. One of the ways you could do this is to use an else block. If the try block calculation of mpg is successful, then you convert the result to a float in the else block before returning:
    #
    # def miles_per_gallon(miles, gallons):
    #     try:
    #         mpg = miles / gallons
    #     except ZeroDivisionError:
    #         mpg = None
    #     except TypeError as exc:
    #         print("you need to provide numbers")
    #         raise exc
    #     else:
    #         mpg = float(mpg) if mpg is not None else mpg
    #     finally:
    #         print(f"miles_per_gallon({miles}, {gallons})")
    #     return mpg
    # Now the results of a call to miles_per_gallon(), if successful, will always be a float.
    #
    # For more on using the else block as part of a try and except block, check out Python Exceptions: An Introduction.

    print ('------------------------------------------------------')
    print ('The assert Keyword')
    print ('------------------------------------------------------')
    # The assert keyword in Python is used to specify an assert statement, or an assertion about an expression. An assert statement will result in a no-op if the expression (<expr>) is truthy, and it will raise an AssertionError if the expression is falsy. To define an assertion, use assert followed by an expression:
    #
    # assert <expr>
    # Generally, you use assert statements to make sure something that needs to be true is. You shouldn’t rely on them for runtime logic, however, as they can be ignored depending on how your Python program is executed.
    #
    # To learn more about the assert keyword, check out the tutorial Python’s assert: Debug and Test Your Code Like a Pro.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_09_Exception_Handling_Keywords ()
#endif

#endmodule
