#------------------------------------------
# Keywords_08_Import_Keywords ():
#------------------------------------------
def Keywords_08_Import_Keywords ():
    """Keywords_08_Import_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Keywords_08_Import_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Import Keywords: import,from,as')
    print ('------------------------------------------------------')
    # Some tools, such as Python keywords and built-in functions, are always available in your program. However, for other tools that aren’t built in, you’ll need to import them. Python’s standard library offers many useful modules that are only an import away. Additionally, PyPI provides a vast collection of third-party libraries and tools that, once you’ve installed them into your environment, you’ll need to import into your programs.
    #
    # The following are brief descriptions of the three Python keywords used for importing modules into your program. For more information about these keywords, check out Python Modules and Packages – An Introduction and Python import: Advanced Techniques and Tips.

    print ('------------------------------------------------------')
    print ('The import Keyword')
    print ('------------------------------------------------------')
    # Python’s import keyword is used to import, or include, a module for use in your Python program. Basic usage syntax looks like this:
    #
    # import <module>
    # After that statement runs, the <module> will be available to your program.
    #
    # For example, if you want to use the Counter class from the collections module in the standard library, then you can use the following code:
    #
    import collections
    collections.Counter()
    # Counter()
    # Importing collections in this way makes the whole collections module, including the Counter class, available to your program. By using the module name, you have access to all the tools available in that module. To get access to Counter, you reference it from the module: collections.Counter.

    print ('------------------------------------------------------')
    print ('The from Keyword')
    print ('------------------------------------------------------')
    # The from keyword is used together with import to import something specific from a module:
    #
    # from <module> import <thing>
    # This will import whatever <thing> is inside <module> to be used inside your program. These two Python keywords, from and import, are used together.
    #
    # If you want to use Counter from the collections module in the standard library, then you can import it specifically:
    #
    from collections import Counter
    Counter()
    # Importing Counter like this makes the Counter class available, but nothing else from the collections module is available. Counter is now available without you having to reference it from the collections module.
    #

    print ('------------------------------------------------------')
    print ('The as Keyword')
    print ('------------------------------------------------------')
    # The as keyword is used to alias an imported module or tool. It’s used together with the Python keywords import and from to change the name of the thing being imported:
    #
    # import <module> as <alias>
    # from <module> import <thing> as <alias>
    # For modules that have really long names or a commonly used import alias, as can be helpful in creating the alias.
    #
    # If you want to import the Counter class from the collections module but name it something different, you can alias it by using as:
    #
    # >>> from collections import Counter as C
    # >>> C()
    # Counter()
    # Now Counter is available to be used in your program, but it’s referenced by C instead. A more common use of as import aliases is with NumPy or pandas packages. These are commonly imported with standard aliases:
    #
    # import numpy as np
    # import pandas as pd
    # This is a better alternative to just importing everything from a module, and it allows you to shorten the name of the module being imported.
    #

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Keywords_08_Import_Keywords ()
#endif

#endmodule
