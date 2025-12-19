#------------------------------------------
# Dicts_dict11_values ():
#------------------------------------------
def Dicts_dict11_values ():
    """Dicts_dict11_values"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Dicts_dict11_values.__name__}')
    print (f'#-----------------------------')

    # Получаем все значения из словаря
    # values() —  метод, который позволяет получить все значения
    # словаря.
    students = {
        'John': 18,
        'Alice': 20,
        'Bob': 19
    }
    #
    ages = students.values ()
    print (ages)


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Dicts_dict11_values ()
#endif

#endmodule
