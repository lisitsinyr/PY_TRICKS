#------------------------------------------
# f-strings_01_ ():
#------------------------------------------
def f-strings_01_ ():
    """f-strings_01_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', f-strings_01_.__name__)
    print ('#-----------------------------')

    # f_string          ::= (literal_char | "{{" | "}}" | replacement_field)*
    #
    # replacement_field ::= "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
    #
    # f_expression      ::= (conditional_expression | "*" or_expr) ("," conditional_expression | "," "*" or_expr)* [","] | yield_expression
    #
    # conversion        ::= "s" | "r" | "a"
    #
    # format_spec       ::= (literal_char | replacement_field)*
    #
    # literal_char      ::= <any code point except "{", "}" or NULL>
    #
    # Explicit Conversion Flag
    #
    # Флаг явного преобразования используется для преобразования
    # значения поля format перед его непосредственным
    # форматированием.
    #
    # Это поле можно использовать для переопределения поведения
    # format для какого либо конкретного типа и форматирования
    # значения. В настоящее время распространены два явных флага
    # преобразования:
    #
    # !r – преобразует значение в строку, используя функцию repr()
    # !s – преобразует значение в строку, используя функцию str()
    #
    # В примере, в случае с флагом !r строка 'Hello' будет
    # напечатана с кавычками в поле шириной не менее 20 символов,
    # а в случае с флагом !s – без кавычек (в более удобном для
    # чтения виде).

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f-strings_01_ ()
#endif

#endmodule
