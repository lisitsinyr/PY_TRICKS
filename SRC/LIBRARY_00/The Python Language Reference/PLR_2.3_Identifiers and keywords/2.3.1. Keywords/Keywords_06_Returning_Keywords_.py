#------------------------------------------
# Keywords_06_Returning_Keywords ():
#------------------------------------------
def Keywords_06_Returning_Keywords ():
    """Keywords_06_Returning_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_06_Returning_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Returning Keywords: return,yield')
    print ('------------------------------------------------------')
    # There are two Python keywords used to specify what gets returned from functions or methods: return and yield. Understanding when and where to use return is vital to becoming a better Python programmer. The yield keyword is a more advanced feature of Python, but it can be a useful tool to understand.

    print ('------------------------------------------------------')
    print ('The return Keyword')
    print ('------------------------------------------------------')
    # Python’s return keyword is valid only as part of a function defined with def. When Python encounters this keyword, it will exit the function at that point and return the results of whatever comes after the return keyword:
    # def <function_name>():
    #     return <expr>
    # When given no expression, return will return None by default:
    def return_none():
        return
    
    r = return_none()
    print(r)
    # None
    # Most of the time, however, you want to return the results of an expression or a specific value:
    def plus_1(num):
       return num + 1
    
    plus_1(9)
    # 10
    r = plus_1(9)
    print(r)
    # 10
    # You can even use the return keyword multiple times in a function. This allows you to have multiple exit points in your function. A classic example of when you would want to have multiple return statements is the following recursive solution to calculating factorial:
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    # In the factorial function above, there are two cases in which you would want to return from the function. The first is the base case, when the number is 1, and the second is the regular case, when you want to multiply the current number by the next number’s factorial value.
    #
    # To learn more about the return keyword, check out The Python return Statement: Usage and Best Practices and Defining Your Own Python Function.

    print ('------------------------------------------------------')
    print ('The yield Keyword')
    print ('------------------------------------------------------')
    # Python’s yield keyword is kind of like the return keyword in that it specifies what gets returned from a function. However, when a function has a yield statement, what gets returned is a generator. The generator can then be passed to Python’s built-in next() to get the next value returned from the function.
    #
    # When you call a function with yield statements, Python executes the function until it reaches the first yield keyword and then returns a generator. These are known as generator functions:
    #
    # def <function_name>():
    #     yield <expr>
    # The most straightforward example of this would be a generator function that returns the same set of values:
    #
    def family():
        yield "Pam"
        yield "Jim"
        yield "Cece"
        yield "Philip"
    
    names = family()
    # >>> names
    # <generator object family at 0x7f47a43577d8>
    next(names)
    # 'Pam'
    next(names)
    # 'Jim'
    next(names)
    # 'Cece'
    next(names)
    # 'Philip'
    next(names)
    # Traceback (most recent call last):
    #   ...
    # StopIteration
    # Once the StopIteration exception is raised, the generator is done returning values. In order to go through the names again, you would need to call family() again and get a new generator. Most of the time, a generator function will be called as part of a for loop, which does the next() calls for you.
    #
    # For much more on the yield keyword and using generators and generator functions, check out How to Use Generators and yield in Python and Python Generators 101.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_06_Returning_Keywords ()
#endif

#endmodule
