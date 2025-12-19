#------------------------------------------
# Keywords_10_Asynchronous_Programming_Keywords ():
#------------------------------------------
def Keywords_10_Asynchronous_Programming_Keywords ():
    """Keywords_10_Asynchronous_Programming_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_10_Asynchronous_Programming_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Asynchronous Programming Keywords: async,await')
    print ('------------------------------------------------------')
    # Asynchronous programming is a complex topic. There are two Python keywords defined to help make asynchronous code more readable and cleaner: async and await.
    #
    # The sections below introduce the two asynchronous keywords and their basic syntax, but don’t cover asynchronous programming in depth. To learn more about asynchronous programming, check out Async IO in Python: A Complete Walkthrough and Getting Started With Async Features in Python.

    print ('------------------------------------------------------')
    print ('The async Keyword')
    print ('------------------------------------------------------')
    # The async keyword is used with def to define an asynchronous function, or coroutine. The syntax is just like defining a function, with the addition of async at the beginning:
    #
    # async def <function>(<params>):
    #     <statements>
    # You can make a function asynchronous by adding the async keyword before the function’s regular definition.

    print ('------------------------------------------------------')
    print ('The await Keyword')
    print ('------------------------------------------------------')
    # Python’s await keyword is used in asynchronous functions to specify a point in the function where control is given back to the event loop for other functions to run. To use it, place await before a call to any async function:
    #
    # await <some async function call>
    # <var> = await <some async function call>
    # When using await, you can either call the asynchronous function and ignore the results, or you can store the results in a variable when the function eventually returns.
    #

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_10_Asynchronous_Programming_Keywords ()
#endif

#endmodule
