#------------------------------------------
# Keywords_03_Operator_Keywords ():
#------------------------------------------
def Keywords_03_Operator_Keywords ():
    """Keywords_03_Operator_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_03_Operator_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Operator Keywords: and,or,not,in,is')
    print ('------------------------------------------------------')
    # Several Python keywords are used as operators. In other programming languages,
    # these operators use symbols like &, |, and !. The Python operators for these are all keywords:
    # Math Operator Python Keyword  Other Languages
    # AND, ∧    and &&
    # OR, ∨ or  ||
    # NOT, ¬    not !
    # CONTAINS, ∈   in
    # IDENTITY  is  ===
    # Python code was designed for readability. That’s why many of the operators that use symbols in other programming languages are keywords in Python.

    print ('------------------------------------------------------')
    print ('The and Keyword')
    print ('------------------------------------------------------')
    # The Python keyword and is used to determine if both the left and right operands are truthy or falsy. If both operands are truthy, then the result will be truthy. If one is falsy, then the result will be falsy:
    # <expr1> and <expr2>
    # Note that the results of an and statement will not necessarily be True or False. This is because of the quirky behavior of and. Rather than evaluating the operands to their Boolean values, and simply returns <expr1> if it is falsy or else it returns <expr2>. The results of an and statement could be passed to bool() to get the explicit True or False value, or they could be used in a conditional if statement.
    #
    # If you wanted to define an expression that did the same thing as an and expression, but without using the and keyword, then you could use the Python ternary operator:
    #
    # left if not left else right
    # The above statement will produce the same result as left and right.
    #
    # Because and returns the first operand if it’s falsy and otherwise returns the last operand, you can also use and in an assignment:
    #
    # x = y and z
    # If y is falsy, then this would result in x being assigned the value of y. Otherwise, x would be assigned the value of z. However, this makes for confusing code. A more verbose and clear alternative would be:
    #
    # x = y if not y else z
    # This code is longer, but it more clearly indicates what you’re trying to accomplish.
    #
    # To learn more about the and keyword, check out the tutorial Using the “and” Boolean Operator in Python .

    print ('------------------------------------------------------')
    print ('The or Keyword')
    print ('------------------------------------------------------')
    # Python’s or keyword is used to determine if at least one of the operands is truthy. An or statement returns the first operand if it is truthy and otherwise returns the second operand:
    #
    # <expr1> or <expr2>
    # Just like the and keyword, or doesn’t convert its operands to their Boolean values. Instead, it relies on their truthiness to determine the results.
    #
    # If you wanted to write something like an or expression without the use of or, then you could do so with a ternary expression:
    #
    # left if left else right
    # This expression will produce the same result as left or right. To take advantage of this behavior, you’ll also sometimes see or used in assignments. This is generally discouraged in favor of a more explicit assignment.
    #
    # For a more in-depth look at or, you can read about how to use the Python or operator.

    print ('------------------------------------------------------')
    print ('The not Keyword')
    print ('------------------------------------------------------')
    # Python’s not keyword is used to get the opposite Boolean value of a variable:
    #
    val = ""  # Truthiness value is `False`
    print (not val)
    # True
    val = 5  # Truthiness value is `True`
    print (val)
    # False
    # The not keyword is used in conditional statements or other Boolean expressions to flip the Boolean meaning or result. Unlike and and or, not will return an explicit Boolean value, True or False.
    #
    # If you wanted to get the same behavior without using not, then you could do so with the following ternary expression:
    #
    # False if <expr> else True
    # This statement would return the same result as not <expr>.
    #
    # To learn more about the not keyword, check out the tutorial Using the “not” Boolean Operator in Python .

    print ('------------------------------------------------------')
    print ('The in Keyword')
    print ('------------------------------------------------------')
    # Python’s in keyword is a powerful containment check, or membership operator. Given an element to find and a container or sequence to search, in will return True or False indicating whether the element was found in the container:
    #
    # <element> in <container>
    # A good example of using the in keyword is checking for a specific letter in a string:
    #
    name = "Chad"
    print ("c" in name)
    # False
    print ("C" in name)
    # True
    # The in keyword works with all types of containers: lists, dicts, sets, strings, and anything else that defines __contains__() or can be iterated over.
    #
    # To learn more about the not keyword, check out the tutorial Python’s “in” and “not in” Operators: Check for Membership .
    #

    print ('------------------------------------------------------')
    print ('The is Keyword')
    print ('------------------------------------------------------')
    # Python’s is keyword is an identity check. This is different from the == operator, which checks for equality. Sometimes, two things can be considered equal but not be the exact same object in memory. The is keyword determines whether two objects are exactly the same object:
    #
    # <obj1> is <obj2>
    # This will return True if <obj1> is the exact same object in memory as <obj2>, or else it will return False.
    #
    # Most of the time, you’ll see is being used to check if an object is None. Since None is a singleton, there’s only one instance of None that can exist, so all None values are the exact same object in memory.
    #
    # If these concepts are new to you, then you can get a more in-depth explanation by checking out Python ‘!=’ Is Not ‘is not’: Comparing Objects in Python. For a deeper dive into how is works, check out Operators and Expressions in Python.
    #

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_03_Operator_Keywords ()
#endif

#endmodule
