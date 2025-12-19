#------------------------------------------
# Keywords_05_Iteration_Keywords ():
#------------------------------------------
def Keywords_05_Iteration_Keywords ():
    """Keywords_05_Iteration_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_05_Iteration_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Iteration Keywords: for,while,break,continue,else')
    print ('------------------------------------------------------')
    # Looping and iteration are hugely important programming concepts. Several Python keywords are used to create and work with loops. These, like the Python keywords used for conditionals, will be used and seen in just about every Python program you come across. Understanding them and their proper usage will help you improve as a Python programmer.

    print ('------------------------------------------------------')
    print ('The for Keyword')
    print ('------------------------------------------------------')
    # The most common loop in Python is the for loop. It’s constructed by combining the Python keywords for and in explained earlier. The basic syntax for a for loop is as follows:
    #
    # for <element> in <container>:
    #     <statements>
    # A common example is looping over the numbers one through five and printing them to the screen:
    #
    for num in range(1, 6):
         print(num)
    # 1
    # 2
    # 3
    # 4
    # 5
    # In many other programming languages, the syntax for a for loop will look a little different. You’ll often need to specify the variable, the condition for continuing, and the way to increment that variable: for (int i = 0; i < 5; i++).
    #
    # In Python, the for loop is like a for-each loop in other programming languages. Given the object to iterate over, it assigns the value of each iteration to the variable:
    #
    people = ["Kevin", "Creed", "Jim"]
    for person in people:
         print(f"{person} was in The Office.")
    # Kevin was in The Office.
    # Creed was in The Office.
    # Jim was in The Office.
    # In this example, you start with a list of people’s names. The for loop starts with the for keyword at the beginning of the line, followed by a variable that stores each list element, then the in keyword, and finally the container, which in this case is people.
    #
    # Python’s for loop is another major ingredient in any Python program. To learn more about for loops, check out Python for Loops: The Pythonic Way.

    print ('------------------------------------------------------')
    print ('The while Keyword')
    print ('------------------------------------------------------')
    # Python’s while loop uses the keyword while and works like a while loop in other programming languages. As long as the condition that follows the while keyword is truthy, the block following the while statement will continue to be executed over and over again:
    #
    # while <expr>:
    #     <statements>
    # Note: For the infinite loop example below, be prepared to use Ctrl+C to stop the process if you decide to try it on your own machine.
    #
    # The easiest way to specify an infinite loop in Python is to use the while keyword with an expression that’s always truthy:

    # while True:
    #      print("working...")

    # For more practical examples of infinite loops in action, check out Socket Programming in Python (Guide). To learn more about while loops, check out Python “while” Loops (Indefinite Iteration).

    print ('------------------------------------------------------')
    print ('The break Keyword')
    print ('------------------------------------------------------')
    # If you need to exit a loop early, then you can use the break keyword. This keyword will work in both for and while loops:
    #
    # for <element> in <container>:
    #     if <expr>:
    #         break
    # An example of using the break keyword would be if you were summing the integers in a list of numbers and wanted to quit when the total went above a given value:
    #
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total_sum = 0
    for num in nums:
         total_sum += num
         if total_sum > 10:
             break
    print (total_sum)
    # 15
    # Both the Python keywords break and continue can be useful tools when working with loops. For a deeper discussion of their uses, check out Python “while” Loops (Indefinite Iteration). If you’d like to explore another use case for the break keyword, then you can learn how to emulate do-while loops in Python.

    print ('------------------------------------------------------')
    print ('The continue Keyword')
    print ('------------------------------------------------------')
    # Python also has a continue keyword for when you want to skip to the next loop iteration. Like in most other programming languages, the continue keyword allows you to stop executing the current loop iteration and move on to the next iteration:
    #
    # for <element> in <container>:
    #     if <expr>:
    #         continue
    # The continue keyword also works in while loops.
    # If the continue keyword is reached in a loop, then the current iteration is stopped,
    # and the next iteration of the loop is started.

    print ('------------------------------------------------------')
    print ('The else Keyword Used With Loops')
    print ('------------------------------------------------------')
    # In addition to using the else keyword with conditional if statements,
    # you can also use it as part of a loop. When used with a loop, the else keyword
    # specifies code that should be run if the loop exits normally, meaning break was not called to exit the loop early.
    # The syntax for using else with a for loop looks like the following:
    # for <element> in <container>:
    #     <statements>
    # else:
    #     <statements>
    # This looks very similar to using else with an if statement. Using else with a while loop is similar:

    # while <expr>:
    #     <statements>
    # else:
    #     <statements>
    # The Python standard documentation has a section on using break and else with a for loop that you should really check out. It uses a great example to illustrate the usefulness of the else block.
    # The task it shows is looping over the numbers two through nine to find the prime numbers. One way you could do this is with a standard for loop with a flag variable:
    for n in range(2, 10):
        prime = True
        for x in range(2, n):
            if n % x == 0:
                prime = False
                print(f"{n} is not prime")
                break
        if prime:
            print(f"{n} is prime!")
    # 2 is prime!
    # 3 is prime!
    # 4 is not prime
    # 5 is prime!
    # 6 is not prime
    # 7 is prime!
    # 8 is not prime
    # 9 is not prime
    # You can use the prime flag to indicate how the loop was exited. If it exited normally, then the prime flag stays True. If it exited with break, then the prime flag will be set to False. Once outside the inner for loop, you can check the flag to determine if prime is True and, if so, print that the number is prime.
    # The else block provides more straightforward syntax. If you find yourself having to set a flag in a loop, then consider the next example as a way to potentially simplify your code:
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} is not prime")
                break
        else:
            print(f"{n} is prime!")
    
    # 2 is prime!
    # 3 is prime!
    # 4 is not prime
    # 5 is prime!
    # 6 is not prime
    # 7 is prime!
    # 8 is not prime
    # 9 is not prime
    # The only thing that you need to do to use the else block in this example is to remove the prime flag and replace the final if statement with the else block. This ends up producing the same result as the example before, only with clearer code.
    # Sometimes using an else keyword with a loop can seem a little strange, but once you understand that it allows you to avoid using flags in your loops, it can be a powerful tool.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_05_Iteration_Keywords ()
#endif

#endmodule
