#------------------------------------------
# Keywords_04_Control_Flow_Keywords ():
#------------------------------------------
def Keywords_04_Control_Flow_Keywords ():
    """Keywords_04_Control_Flow_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_04_Control_Flow_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Control Flow Keywords: if,elif,else')
    print ('------------------------------------------------------')
    # Three Python keywords are used for control flow: if, elif, and else. These Python keywords allow you to use conditional logic and execute code given certain conditions. These keywords are very common—they’ll be used in almost every program you see or write in Python.

    print ('------------------------------------------------------')
    print ('The if Keyword')
    print ('------------------------------------------------------')
    # The if keyword is used to start a conditional statement. An if statement allows you to write a block of code that gets executed only if the expression after if is truthy.
    #
    # The syntax for an if statement starts with the keyword if at the beginning of the line, followed by a valid expression that will be evaluated for its truthiness value:
    #
    # if <expr>:
    #     <statements>
    # The if statement is a crucial component of most programs. For more information about the if statement, check out Conditional Statements in Python.
    #
    # Another use of the if keyword is as part of Python’s ternary operator:
    #
    # <var> = <expr1> if <expr2> else <expr3>
    # This is a one-line version of the if...else statement:
    #
    # if <expr2>:
    #     <var> = <expr1>
    # else:
    #     <var> = <expr3>
    # If your expressions are straightforward, then using the ternary expression provides a nice way to simplify your code a bit. Once the conditions get a little complex, it’s often better to rely on the standard if statement.

    print ('------------------------------------------------------')
    print ('The elif Keyword')
    print ('------------------------------------------------------')
    # The elif statement looks and functions like the if statement, with two major differences:
    #
    # Using elif is only valid after an if statement or another elif.
    # You can use as many elif statements as you need.
    # In other programming languages, elif appears as either else if, written as two separate words, or elseif, written as one word:
    #
    # if <expr1>:
    #     <statements>
    # elif <expr2>:
    #     <statements>
    # elif <expr3>:
    #     <statements>
    # Python doesn’t have a switch statement. One way to get the same functionality that other programming languages provide with switch statements is by using if and elif. For other ways of reproducing the switch statement in Python, check out Emulating switch/case Statements in Python and Structural Pattern Matching in Python.

    print ('------------------------------------------------------')
    print ('The else Keyword')
    print ('------------------------------------------------------')
    # The else statement, in conjunction with the Python keywords if and elif, denotes a block of code that should be executed only if the other conditional blocks, if and elif, are all falsy:
    #
    # if <expr>:
    #     <statements>
    # else:
    #     <statements>
    # Notice that the else statement doesn’t take a conditional expression. Knowledge of the elif and else keywords and their proper usage is critical for Python programmers. Together with if, they make up some of the most frequently used components in any Python program.
    #

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_04_Control_Flow_Keywords ()
#endif

#endmodule
