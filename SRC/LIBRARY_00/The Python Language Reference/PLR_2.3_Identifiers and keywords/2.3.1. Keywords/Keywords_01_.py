#------------------------------------------
# keywords_01_ ():
#------------------------------------------
def keywords_01_ ():
    """keywords_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {keywords_01_.__name__}')
    print (f'#-----------------------------')

    # Python Keywords: An Introduction
    # by Chad Hansen  Feb 12, 2025 3 Comments
    # https://realpython.com/python-keywords/#python-keywords

    #  Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: Exploring Keywords in Python
    #
    # Python keywords are reserved words with specific functions and restrictions in the language. Currently, Python has thirty-five keywords and four soft keywords. These keywords are always available in Python, which means you don’t need to import them. Understanding how to use them correctly is fundamental for building Python programs.
    #
    # By the end of this tutorial, you’ll understand that:
    #
    # There are 35 keywords and four soft keywords in Python.
    # You can get a list of all keywords using keyword.kwlist from the keyword module.
    # Soft keywords in Python act as keywords only in specific contexts.
    # print and exec are keywords that have been deprecated and turned into functions in Python 3.
    # In this article, you’ll find a basic introduction to all Python keywords and soft keywords along with other resources that will be helpful for learning more about each keyword.
    #
    # Get Your Cheat Sheet: Click here to download a free cheat sheet that summarizes the main keywords in Python.
    #
    #  Take the Quiz: Test your knowledge with our interactive “Python Keywords: An Introduction” quiz. You’ll receive a score upon completion to help you track your learning progress:
    
    #------------------------------------------------------
    # Soft Keywords and Their Usage
    # As mentioned before, soft keywords are contextual. They act as keywords only in specific contexts. That means you may encounter these names in code where they act as variable or function names.
    #------------------------------------------------------
    #
    # When soft keywords are used in their intended context, they act just like any other keyword.

    #------------------------------------------------------
    # How to Identify Python Keywords
    #------------------------------------------------------
    # The list of Python keywords has changed over time. For example, the await and async keywords weren’t added until Python 3.7. Also, both print and exec were keywords in Python 2.7 but were turned into built-in functions in Python 3 and no longer appear in the list of keywords.
    #
    # Soft keywords were introduced in Python 3.10. Back then, there was only case, match, and _. The type soft keyword was added in Python 3.12.
    #
    # In the following sections, you’ll learn several ways to identify which words are keywords, and which soft keywords are available in the Python version you’re using.
    #
    # Leverage the Syntax Highlighting of Your IDE
    # There are a lot of good Python IDEs out there. All of them will highlight keywords to differentiate them from other words in your code. This will help you quickly identify Python keywords while you’re programming so you don’t use them incorrectly.
    
    #------------------------------------------------------
    # Use Code in a REPL to Check Keywords
    #------------------------------------------------------
    # In the Python REPL, there are a number of ways you can identify valid Python keywords and learn more about them.
    
    #------------------------------------------------------
    # You can get a list of available keywords by using help():
    #------------------------------------------------------
    help("keywords")
    #
    # Here is a list of the Python keywords.  Enter any keyword to get more help.
    #
    # False               class               from                or
    # None                continue            global              pass
    # True                def                 if                  raise
    # and                 del                 import              return
    # as                  elif                in                  try
    # assert              else                is                  while
    # async               except              lambda              with
    # await               finally             nonlocal            yield
    # break               for                 not

    #------------------------------------------------------
    # Next, as indicated in the output above, you can use help() again by passing in the specific keyword that you need more information about. You can do this, for example, with the pass keyword:
    #------------------------------------------------------
    help("pass")
    # The "pass" statement
    # ********************
    #
    #    pass_stmt ::= "pass"
    #
    # "pass" is a null operation — when it is executed, nothing happens. It
    # is useful as a placeholder when a statement is required syntactically,
    # but no code needs to be executed, for example:
    #
    #    def f(arg): pass    # a function that does nothing (yet)
    #
    #    class C: pass       # a class with no methods (yet)
    
    #------------------------------------------------------
    # Python also provides a keyword module for working with Python keywords in a programmatic way. The keyword module has four helpful members for dealing with keywords:
    #------------------------------------------------------
    # kwlist provides a list of all the Python keywords for the version of Python you’re running.
    # iskeyword() provides a handy way to determine if a string is also a keyword.
    # softkwlist provides a list of all soft keywords in Python for the version of Python you’re running.
    # issoftkeyword() allows you to determine if a string is also a soft keyword.
    # To get a list of all the keywords in the version of Python you’re running, and to quickly determine how many keywords are defined, use keyword.kwlist:
    import keyword
    keyword.kwlist
    # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', ...
    # >>> len(keyword.kwlist)
    # 35
    # >>> keyword.iskeyword("type")
    # False
    # >>> keyword.issoftkeyword("type")
    # True
    # >>> keyword.softkwlist
    # ['_', 'case', 'match', 'type']
    # If you need to know more about keywords or work with them in a programmatic way, then you can use this documentation and tooling that Python provides for you.
    #
    # Look for a SyntaxError
    # Finally, another indicator that a word you’re using is actually a keyword is if you get a SyntaxError while trying to assign to it, name a function with it, or do something else that isn’t allowed with it. This one is a little harder to spot, but it’s a way that Python will let you know you’re using a keyword incorrectly.
    
    #------------------------------------------------------
    # Deprecated Python Keywords
    #------------------------------------------------------
    # Sometimes a Python keyword becomes a built-in function. That was the case with both print and exec. These used to be Python keywords in version 2.7, but they’ve since been changed to built-in functions.
    
    #------------------------------------------------------
    # The Former print Keyword
    #------------------------------------------------------
    # When print was a keyword, the syntax to print something to the screen looked like this:
    # print "Hello, World"
    # Notice that it looks like a lot of the other keyword statements, with the keyword followed by the arguments.
    # Now print is no longer a keyword, and printing is accomplished with the built-in print(). To print something to the screen, you now use the following syntax:
    print("Hello, World")
    # For more on printing, check out Your Guide to the Python print() Function.
    
    #------------------------------------------------------
    # The Former exec Keyword
    #------------------------------------------------------
    # In Python 2.7, the exec keyword took Python code as a string and executed it. This was done with the following syntax:
    #
    # exec "<statements>"
    # You can get the same behavior in Python 3+, only with the built-in exec(). For example, if you wanted to execute "x = 12 * 7" in your Python code, then you could do the following:
    #
    exec("x = 12 * 7")
    # >>> x == 84
    # True
    # For more on exec() and its uses, check out How to Run Your Python Scripts and Code and Python’s exec(): Execute Dynamically Generated Code.
    
    #------------------------------------------------------
    # Conclusion
    #------------------------------------------------------
    # Python keywords are the fundamental building blocks of any Python program. Understanding their proper use is key to improving your skills so you can write more efficient and readable code.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    keywords_01_ ()
#endif

#endmodule
