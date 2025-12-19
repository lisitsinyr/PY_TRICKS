#------------------------------------------
# Keywords_07_Structure_Keywords ():
#------------------------------------------
def Keywords_07_Structure_Keywords ():
    """Keywords_07_Structure_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_07_Structure_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Structure Keywords: def,class,with,as,pass,lambda')
    print ('------------------------------------------------------')
    # In order to define functions and classes or use context managers, you’ll need to use one of the Python keywords in this section. They’re an essential part of the Python language, and understanding when to use them will help you become a better Python programmer.

    print ('------------------------------------------------------')
    print ('The def Keyword')
    print ('------------------------------------------------------')
    # Python’s keyword def is used to define a function or method of a class. This is equivalent to function in JavaScript and PHP. The basic syntax for defining a function with def looks like this:
    #
    # def <function>(<params>):
    #     <body>
    # Functions and methods can be very helpful structures in any Python program. To learn more about defining them and all their ins and outs, check out Defining Your Own Python Function.

    print ('------------------------------------------------------')
    print ('The class Keyword')
    print ('------------------------------------------------------')
    # To define a class in Python, you use the class keyword. The general syntax for defining a class with class is as follows:
    #
    # class ClassName(<extends>):
    #     <body>
    # Classes are powerful tools in object-oriented programming, and you should know about them and how to define them. To learn more, check out Python Classes: The Power of Object-Oriented Programming and Object-Oriented Programming (OOP) in Python.

    print ('------------------------------------------------------')
    print ('The with Keyword')
    print ('------------------------------------------------------')
    # Context managers are a really helpful structure in Python. Each context manager executes specific code before and after the statements you specify. To use one, you use the with keyword:
    #
    # with <context manager> as <var>:
    #     <statements>
    # Using with gives you a way to define code to be executed within the context manager’s scope. The most basic example of this is when you’re working with file I/O in Python.
    #
    # If you wanted to open a file, do something with that file, and then make sure that the file was closed correctly, then you would use a context manager. Consider this example in which names.txt contains a list of names, one per line:
    with open ("names.txt") as input_file:
        for name in input_file:
            print (name.strip ())

    # Jim
    # Pam
    # Cece
    # Philip
    # The file I/O context manager provided by open() and initiated with the with keyword opens the file for reading, assigns the open file pointer to input_file, then executes whatever code you specify in the with block. Then, after the block is executed, the file pointer closes. Even if your code in the with block raises an exception, the file pointer would still close.
    # For a great example of using with and context managers, check out Python Timer Functions: Three Ways to Monitor Your Code or dive deeper in the tutorial Context Managers and Python’s with Statement.
    # The as Keyword Used With with
    # If you want access to the results of the expression or context manager passed to with, you’ll need to alias it using as. You may have also seen as used to alias imports and exceptions, and this is no different. The alias is available in the with block:
    # with <expr> as <alias>:
    #     <statements>
    # Most of the time, you’ll see these two Python keywords, with and as, used together.

    # ------------------------------------------------------
    print ('The pass Keyword')
    # ------------------------------------------------------
    # Since Python doesn’t have block indicators to specify the end of a block, the pass keyword is used to specify that the block is intentionally left blank. It’s the equivalent of a no-op, or no operation. Here are a few examples of using pass to specify that the block is blank:
    def empty_function ():
        pass

    class EmptyClass:
        pass

    if True:
        pass
    # For more on pass, check out The pass Statement: How to Do Nothing in Python.

    print ('------------------------------------------------------')
    print ('The lambda Keyword')
    print ('------------------------------------------------------')
    # The lambda keyword is used to define a function that doesn’t have a name and has only one expression, the results of which are returned. Functions defined with lambda are referred to as lambda functions:
    #
    # lambda <args>: <expression>
    # A basic example of a lambda function that computes the argument raised to the power of 10 would look like this:
    #
    p10 = lambda x: x ** 10

    # This is equivalent to defining a function with def:
    #
    def p10 (x):
        return x ** 10

    # One common use for a lambda function is specifying a different behavior for another function. For example, imagine you wanted to sort a list of strings by their integer values. The default behavior of sorted() would sort the strings alphabetically. But with sorted(), you can specify which key the list should be sorted on.
    #
    # A lambda function provides a nice way to do so:
    #
    ids = ["id1", "id2", "id30", "id3", "id20", "id10"]
    sorted (ids)
    # ['id1', 'id10', 'id2', 'id20', 'id3', 'id30']
    sorted (ids, key=lambda x: int (x [2:]))

    # ['id1', 'id2', 'id3', 'id10', 'id20', 'id30']
    # This example sorts the list based not on alphabetical order but on the numerical order of the last characters of the strings after converting them to integers. Without lambda, you would have had to define a function, give it a name, and then pass it to sorted(). Using lambda made this code cleaner.
    # For comparison, this is what the example above would look like without using lambda:
    def sort_by_int (x):
        return int (x [2:])

    ids = ["id1", "id2", "id30", "id3", "id20", "id10"]
    sorted (ids, key=sort_by_int)
    # ['id1', 'id2', 'id3', 'id10', 'id20', 'id30']
    # This code produces the same result as the lambda example, but you need to define the function before using it.
    # For a lot more information about lambda, check out How to Use Python Lambda Functions.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_07_Structure_Keywords ()
#endif

#endmodule
