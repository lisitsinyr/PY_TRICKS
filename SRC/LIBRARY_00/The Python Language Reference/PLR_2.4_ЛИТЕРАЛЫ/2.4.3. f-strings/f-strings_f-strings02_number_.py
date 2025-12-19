#------------------------------------------
# f_strings_f_strings02_number ():
#------------------------------------------
def f_strings_f_strings02_number ():
    """f_strings_f_strings02_number"""
#beginfunction
    print ('#-----------------------------')
    print ('#', number_test.__name__)
    print ('#-----------------------------')

    #------------------------------------------
    #
    #------------------------------------------
    vartest_int: int = 100
    print ('vartest_int default  :', vartest_int)
    vartest_float: float = 100.25
    print ('vartest_float default:', vartest_float)
    number = 1000000
    print ('number default       :', number)
    #------------------------------------------
    # :<    Left aligns the result (within the available space)
    print(f'number: {number:<20}')
    # :>    Right aligns the result (within the available space)
    print(f'number: {number:>20d}')
    # :^    Center aligns the result (within the available space)
    print(f'number: {number:.^20}')
    #------------------------------------------
    # :=    Places the sign to the left most position
    print(f'number: {number:=}')
    # :+    Use a plus sign to indicate if the result is positive or negative
    print(f'number: {number:+}')
    # :-    Use a minus sign for negative values only
    print(f'number: {number:-}')
    # :     Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
    print(f'number: {number:}')
    # :,    Use a comma as a thousand separator
    print(f'number: {number:,}')
    # :_    Use a underscore as a thousand separator
    print(f'number: {number:_}')
    # :c    Converts the value into the corresponding Unicode character
    print(f'number: {number:c}')
    #------------------------------------------
    # :<D    Left aligns the result (within the available space)
    #------------------------------------------
    #+ :d    Decimal format
    print(f'number: {number:d}')
    #+ :n    Number format
    print(f'number: {number:n}')
    #+ :%    Percentage format
    print(f'number: {500000/number:.0%}')
    #+ :g    General format
    print(f'number: {number:g}')
    #+ :G    General format (using a upper case E for scientific notations)
    print(f'number: {number:G}')
    #------------------------------------------
    # decimal places
    #------------------------------------------
    #+ :f    Fix point number format
    print(f'number: {number:.2f}')
    #+ :F    Fix point number format, in uppercase format (show inf and nan as INF and NAN)
    print(f'number: {number:.2F}')
    #------------------------------------------
    # hex conversion
    #------------------------------------------
    #+ :x    Hex format, lower case
    print(f'hex: {number:#0x}')
    #+ :X    Hex format, upper case
    print(f'hex: {number:#0X}')
    #------------------------------------------
    # binary conversion
    #------------------------------------------
    #+ :b    Binary format
    print(f'binary: {number:b}')
    #------------------------------------------
    # octal conversion
    #------------------------------------------
    #+ :o    Octal format
    print(f'octal: {number:o}')
    #------------------------------------------
    # scientific notation
    #------------------------------------------
    #+ :e    Scientific format, with a lower case e
    print(f'scientific: {number:e}')
    #+ :E    Scientific format, with an upper case E
    print(f'scientific: {number:E}')
    #------------------------------------------
    # total number of characters
    #------------------------------------------
    print(f'Number: {number:09}')
    #------------------------------------------
    print(f'Number: {100!r}')
    #------------------------------------------

    #------------------------------------------
    #
    #------------------------------------------
    apple_marketcap = 2.626 * 10e12
    print(f'{apple_marketcap = :,}') # comma separator
    percentage = 10.394394
    print(f'{percentage = :.2%}') # percentage

    #------------------------------------------
    #
    #------------------------------------------
    number = 4
    print ('number default:', number)
    print(f'number:{number:4}') # width of 10

    #------------------------------------------
    # numbers
    #------------------------------------------
    for number in range(1, 5):
        print(f'the number:{number:{number}}')

    #------------------------------------------
    #
    #------------------------------------------
    price = 59
    txt = f'The price is {price:.2f} dollars'
    print(txt)

    #------------------------------------------
    # You can also format a value directly without keeping it in a variable:
    #------------------------------------------
    txt = f'The price is {95:.2f} dollars'
    print (txt)

    #------------------------------------------
    # You can perform Python operations inside the placeholders.
    #------------------------------------------
    txt = f'The price is {20 * 59} dollars'
    print (txt)

    #------------------------------------------
    # You can perform math operations on variables:
    #------------------------------------------
    price = 59
    tax = 0.25
    txt = f'The price is {price + (price * tax)} dollars'
    print (txt)

    #------------------------------------------
    #
    #------------------------------------------
    print (f'5 + 3 = {5 + 3}')

    #------------------------------------------
    #
    #------------------------------------------
    import decimal
    width = 10
    precision = 4
    value = decimal.Decimal('12.34567')
    print(f'{value:{width}.{precision}}')  #12.35

    #------------------------------------------
    #
    #------------------------------------------
    width = 10
    precision = 4
    value = 12.34567
    print(f'{value:{width}.{precision}}')  #12.35

    #------------------------------------------
    # Форматирование чисел и специальных значений
    #------------------------------------------
    # Чтобы управлять количеством отображаемых десятичных знаков с помощью f-строки, используйте синтаксис f'{value:.nf}', где value — число с плавающей точкой, n — количество десятичных знаков, а f (после .) обозначает форматирование float.
    pi = 3.1415926535
    print(f'Pi rounded to 2 decimal places: {pi:.2f}')
    print(f'Pi rounded to 4 decimal places: {pi:.4f}')
    print(f'Pi rounded to 0 decimal places: {pi:.0f}')

    # Вы можете использовать f-строку для форматирования процентов, используя синтаксис :.n%, где n — количество десятичных знаков.
    score = 0.875
    print(f"Success rate: {score:.2%}")

    # С помощью f-строк можно форматировать и валюту, используя :, для разделения тысяч и .nf для управления десятичными знаками. Вы также можете включить символ валюты, например $, € или £, непосредственно в строку.
    amount = 98765.4321
    print(f"USD: ${amount:,.2f}")
    print(f"EUR: €{amount:,.2f}")
    print(f"GBP: £{amount:,.2f}")

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    f_strings_f_strings02_number ()
#endif

#endmodule
