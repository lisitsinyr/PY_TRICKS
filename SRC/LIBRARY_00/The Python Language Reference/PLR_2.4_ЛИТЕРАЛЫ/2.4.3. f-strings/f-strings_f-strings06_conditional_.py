#------------------------------------------
# f_strings_f_strings06_conditional ():
#------------------------------------------
def f_strings_f_strings06_conditional ():
    """f_strings_f_strings06_conditional"""
#beginfunction
    print ('#-----------------------------')
    print ('#', f_strings_f_strings06_conditional.__name__)
    print ('#-----------------------------')

    #------------------------------------------
    #
    #------------------------------------------
    my_str = 'bobbyhadz.com'
    # ✅ f-string formatting with a condition
    result = f'Result: {my_str.upper() if len(my_str) > 1 else my_str.capitalize()}'
    print(result)  # 👉️ Result: BOBBYHADZ.COM

    #------------------------------------------
    # You can perform if...else statements inside the placeholders:
    #------------------------------------------
    price = 49
    txt = f'It is very {'Expensive' if price > 50 else 'Cheap'}'
    print (txt)

    #------------------------------------------
    #
    #------------------------------------------
    f_expression = 'test expression'
    # f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
    # replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
    # f_expression      ::=  (conditional_expression | "*" or_expr) ("," conditional_expression | "," "*" or_expr)* [","] | yield_expression
    # print(f'{f_expression!a}')
    print(f'{f_expression=!a:<30}')
    # print(replacement_field)

    #------------------------------------------
    #
    #------------------------------------------
    print(f'{(5 > 2) , (6 > 5) =!a:<30}')

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f_strings_f_strings06_conditional ()
#endif

#endmodule
