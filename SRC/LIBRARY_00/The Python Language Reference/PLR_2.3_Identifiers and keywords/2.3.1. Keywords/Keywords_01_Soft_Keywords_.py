#------------------------------------------
# keywords_01_Soft_Keywords ():
#------------------------------------------
def keywords_01_Soft_Keywords ():
    """Keywords_01_Soft_Keywords"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {keywords_01_Soft_Keywords.__name__}')
    print (f'#-----------------------------')

    print ('------------------------------------------------------')
    print ('Soft Keywords: _,case,match,type')
    print ('------------------------------------------------------')
    # As mentioned above, you’ll get an error if you try to assign something to a Python keyword. Soft keywords, on the other hand, aren’t that strict. They syntactically act as keywords only in certain conditions.
    # This new capability was made possible thanks to the introduction of the PEG parser in Python 3.9, which changed how the interpreter reads the source code.
    # Leveraging the PEG parser allowed for the introduction of structural pattern matching in Python. In order to use intuitive syntax, the authors picked match, case, and _ for the pattern matching statements. Notably, match and case are widely used for this purpose in many other programming languages.
    # To prevent conflicts with existing Python code that already used match, case, and _ as variable or function names, Python developers decided to introduce the concept of soft keywords.
    # Currently, there are four soft keywords in Python:
    # _,case,match,type
    # You can use the links above to jump to the soft keywords you’d like to read about, or you can continue reading for a guided tour.

    print ('------------------------------------------------------')
    print ('The match, case, and _ (underscore) soft keywords are used for structural pattern matching)')
    print ('------------------------------------------------------')
    def sum_ingredients(ingredient_counts):
        match ingredient_counts:
            case []:
                return 0
            case [first, *rest]:
                return first + sum_ingredients(rest)
            case _:
                raise ValueError(f"Can only sum lists.")
    # You start with a match statement that specifies what you want to match. Then, one or several case statements follow. Each case describes one pattern.
    # The indented block beneath it says what should happen if there’s a match. You can use the _ as a wildcard pattern that matches anything without binding it to a name.
    result = sum_ingredients([])
    print (f'{result=}')
    result = sum_ingredients([1, 2, 3, 4, 5, 6])
    print (f'{result=}')

    print ('------------------------------------------------------')
    print ('The type Soft Keyword')
    print ('------------------------------------------------------')
    # When you see the word “type”, you might think of the built-in type() function. However, since Python 3.12, type is also a soft keyword.
    # When you use type as a type alias defintinion, type becomes a keyword:
    import random
    type CardDeck = list[tuple[str, int]]
    def shuffle(deck: CardDeck) -> CardDeck:
        return random.sample(deck, k=len(deck))
    # With a type statement like this, you can define an alias to be more descriptive about your data structures.

    result = shuffle([(1, 2), (2, 3), (3, 4)])
    print (f'{result=}')

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    keywords_01_Soft_Keywords ()
#endif

#endmodule
