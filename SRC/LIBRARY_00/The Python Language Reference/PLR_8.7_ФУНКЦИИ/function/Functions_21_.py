#------------------------------------------
# Functions_21_ ():
#------------------------------------------
def Functions_21_ ():
    """Functions_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Functions_21_.__name__)
    print ('#-----------------------------')

    # A Roadmap to Python Parameter Definitions: Best Practices and Beyond
    # Mr Stucknet
    # Mr Stucknet
    #
    # ·
    # Follow
    #
    # 5 min read
    # ·
    # May 20
    #
    #
    #
    #
    # Function parameters can be classified into five groups:
    #
    # Positional or keyword parameters: allow both positional and keyword
    # arguments
    #
    # Variable positional parameters: collect an arbitrary number of positional
    # arguments in a tuple
    #
    # Variable keyword parameters: collect an arbitrary number of keyword
    # arguments in a dictionary
    #
    # Positional-only parameters: can only be passed as positional arguments
    #
    # Keyword-only parameters: can only be passed as keyword arguments
    #
    # All the parameters in the examples we have seen so far in this chapter are normal positional or keyword parameters. We’ve seen how they can be passed as both positional and keyword arguments. There’s not much more to say about them, so let’s look at the other categories. Before we do though, let’s briefly look at optional parameters.
    #
    # Optional parameters:
    # Apart from the categories we’ve looked at here, parameters can also be classified as either required or optional. Optional parameters have a default value specified in the function definition. The syntax is name=value:
    #
    # # parameters.default.py
    # def func(a, b=4, c=88):
    #   print(a, b, c)
    # func(1)
    # func(b=5, a=7, c=9)
    # func(42, c=9)
    # func(42, 43, 44)
    # # prints: 1 4 88
    # # prints: 7 5 9
    # # prints: 42 4 9
    # # prints: 42, 43, 44
    # Here, a is required, while b has the default value 4 and c has the default value 88. It’s important to note that, with the exception of keyword-only parameters, required parameters must always be to the left of all optional parameters in the function definition. Try removing the default value from c in the above example and see for yourself what happens.
    #
    # Variable positional parameters:
    # Sometimes you may prefer not to specify the exact number of positional parameters to a function; Python provides you with the ability to do this by using variable positional parameters. Let’s look at a very common use case, the minimum() function. This is a function that calculates the minimum of its input values:
    #
    # # parameters.variable.positional.py
    # def minimum(*n):
    # # print(type(n)) # n is a tuple
    #   if n: # explained after the code
    #     mn = n[0]
    #     for value in n[1:]:
    #       if value < mn:
    #         mn = value
    #     print(mn)
    # minimum(1, 3, -7, 9)
    # minimum()
    # Asyou can see, when we define a parameter with an asterisk, *, prepended to its name, we are telling Python that this parameter will collect a variable number of positional arguments when the function is called. Within the function, n is a tuple. Uncomment print(type(n)) to see for yourself, and play around with it for a bit.
    #
    # Note that a function can have at most one variable positional parameter — it wouldn’t make sense to have more. Python would have no way of deciding how to divide up the arguments between them. You are also unable to specify a default value for a variable positional parameter. The default value is always an empty tuple.
    #
    # Note:
    #
    # Have you noticed how we checked whether n wasn’t empty with
    # a simple if n:? This is because collection objects evaluate to True
    # when non-empty, and otherwise False, in Python. This is the case
    # for tuples, sets, lists, dictionaries, and so on.
    # One other thing to note is that we may want to throw an error
    # when we call the function with no parameters, instead of silently
    # doing nothing. In this context, we’re not concerned about making
    # this function robust, but rather understanding variable positional
    # parameters.
    #
    # Did you notice that the syntax for defining variable positional parameters looks very much like the syntax for iterable unpacking? This is no coincidence. After all, the two features mirror each other. They are also frequently used together, since variable positional parameters save you from worrying whether the length of the iterable you’re unpacking matches the number of parameters in the function definition.
    #
    # Variable keyword parameters:
    # Variable keyword parameters are very similar to variable positional parameters. The only difference is the syntax (** instead of *) and the fact that they are collected in a dictionary:
    #
    # # parameters.variable.keyword.py
    # def func(**kwargs):
    #   print(kwargs)
    # func(a=1, b=42) # prints {'a': 1, 'b': 42}
    # func() # prints {}
    # func(a=1, b=46, c=99) # prints {'a': 1, 'b': 46, 'c': 99}
    # You can see that adding ** in front of the parameter name in the function definition tells Python to use that name to collect a variable number of keyword parameters. As in the case of variable positional parameters, each function can have at most one variable keyword parameter — and you cannot specify a default value
    #
    # Just like variable positional parameters resemble iterable unpacking, variable keyword parameters resemble dictionary unpacking. Dictionary unpacking is also often used to pass arguments to functions with variable keyword parameters.
    #
    # The reason why being able to pass a variable number of keyword arguments is so important may not be evident at the moment, so how about a more realistic example? Let’s define a function that connects to a database: we want to connect to a default database by simply calling this function with no parameters. We also want to connect to any other database by passing to the function the appropriate parameters. Before
    # you read on, try to spend a couple of minutes figuring out a solution by yourself:
    #
    # # parameters.variable.db.py
    # def connect(**options):
    #   conn_params = {
    #     'host': options.get('host', '127.0.0.1'),
    #     'port': options.get('port', 5432),
    #     'user': options.get('user', ''),
    #     'pwd': options.get('pwd', ''),
    # }
    #   print(conn_params)
    # # we then connect to the db (commented out)
    # # db.connect(**conn_params)
    # connect()
    # connect(host='127.0.0.42', port=5433)
    # connect(port=5431, user='fab', pwd='gandalf')
    # Note that, in the function, we can prepare a dictionary of connection parameters (conn_params) using default values as fallbacks, allowing them to be overwritten if they are provided in the function call. There are better ways to do this with fewer lines of code, but we’re not concerned with that right now. Running the preceding code yields the following result:
    #
    # $ python parameters.variable.db.py
    # {'host': '127.0.0.1', 'port': 5432, 'user': '', 'pwd': ''}
    # {'host': '127.0.0.42', 'port': 5433, 'user': '', 'pwd': ''}
    # {'host': '127.0.0.1', 'port': 5431, 'user': 'fab', 'pwd': 'gandalf'}
    # Note the correspondence between the function calls and the output, and how default values are overridden according to what was passed to the function.

#endfunction
#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Functions_21_ ()
#endif

#endmodule
