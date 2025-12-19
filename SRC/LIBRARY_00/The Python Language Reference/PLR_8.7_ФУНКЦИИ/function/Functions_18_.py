#------------------------------------------
# Functions_18_ ():
#------------------------------------------
def Functions_18_ ():
    """Functions_18_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Functions_18_.__name__)
    print ('#-----------------------------')

    # 4 Types of Function Arguments in Python that You Might Not Know About (29/100 Days of Python)
    # Martin Mirakyan
    # Martin Mirakyan
    #
    # ·
    # Follow
    #
    # 6 min read
    # ·
    # Jan 30
    #
    #
    #
    #
    # Day 29 of the “100 Days of Python” blog post series covering different types of function arguments
    # Python is a powerful programming language that offers multiple ways to call functions. In this tutorial, we will explore 4 different types of function arguments and discuss their use cases by implementing them. We will also look at some real-world examples of functions and discuss the nuances of each type of argument to help you optimize your code for readability and maintainability.
    #
    # Default Arguments in Python
    # Default arguments play a crucial role in Python functions. They provide a default value for a parameter in case no value is passed for that parameter in the function call. The default value is used when no value is specified for the parameter in the function call. This allows you to write functions with a flexible number of arguments and makes the code more readable and maintainable.
    #
    # def area(length, width = 1):
    #     return length * width
    #
    # print(area(5))     # 5
    # print(area(5, 10)) # 50
    # In the first call to the area function, we only passed the length argument. So, the width argument is assigned the default value of 1. In the second call, both length and width arguments are passed, and the function returns the expected result.
    #
    # It’s important to note that default arguments must always follow positional arguments. For example, the following code is invalid:
    #
    # def sum_numbers(a=1, b):
    #     return a + b
    # In this example, the function sum_numbers takes two parameters, a and b, but the default value is specified for a instead of b. This will result in a SyntaxError. To make this code valid, we need to move the default argument after all the positional arguments:
    #
    # def sum_numbers(b, a=1):
    #     return a + b
    # Positional Arguments in Python
    # Positional arguments are the most basic type of arguments in Python. They are passed to a function by matching their position in the function call with the position of the parameters in the function definition. Consider the following example:
    #
    # def greeting(name, title='Mr.'):
    #     return f'Hello, {title} {name}'
    #
    # print(greeting('John'))         # Hello, Mr. John
    # print(greeting('Jack', 'Dr.'))  # Hello, Dr. Jack
    # In this example, the function greeting takes two parameters: name and title, with title having a default value of 'Mr.'. The function call greeting('John') passes one positional argument, 'John', which is assigned to the name parameter. The title parameter is assigned the default value of 'Mr.'.
    #
    # It’s important to note that positional arguments must be passed in the order they are defined in the function definition:
    #
    # def sum_numbers(a, b):
    #     return a + b
    #
    # print(sum_numbers(1, 2)) # 3
    # print(sum_numbers(2, 1)) # 3
    # In this example, the function sum_numbers takes two parameters, a and b, which are used to calculate the sum. The function call sum_numbers(1, 2) passes two positional arguments, 1 and 2, which are assigned to the a and b parameters, respectively. The function call sum_numbers(2, 1) passes two positional arguments, 2 and 1, which are assigned to the a and b parameters, respectively. So, the order of the arguments passed matches exactly the order of the defined function arguments.
    #
    # Keyword Arguments in Python
    # Keyword arguments are arguments passed to a function using the keyword-value pair syntax. Keyword arguments allow you to pass arguments to a function by explicitly specifying the name of the parameter and its value. This makes it easier to understand what each argument does, especially when you have a lot of arguments with complex names or multiple default values. Consider the following example:
    #
    # def greeting(name, title='Mr.'):
    #     return f"Hello, {title} {name}"
    #
    # print(greeting(name='John'))               # Hello, Mr. John
    # print(greeting(name='John', title='Dr.'))  # Hello, Dr. John
    # In this example, the function greeting takes two parameters, name and title, with title having a default value of 'Mr.'. The function call greeting(name='John') passes one keyword argument, name='John', which is assigned to the name parameter. The title parameter is assigned the default value of 'Mr.'. The function call greeting(name='John', title='Dr.') passes two keyword arguments, name='John' and title='Dr.', which are assigned to the name and title parameters, respectively.
    #
    # It’s important to note that keyword arguments can have an arbitrary order, irrespective of the function definition. This is especially useful for functions with many arguments that have a lot of default arguments in their definitions, and we only need to change one or two values in the function call. It also makes it easier to read the code and quickly understand what the function is doing. In such cases, we can use keyword arguments to pass only the values we need, making the function call more readable and easier to maintain. Additionally, keyword arguments can be mixed with positional arguments in the same function call, which makes it easier to use functions in a flexible and efficient way:
    #
    # def create_person(first_name, last_name, age=18, city='London', country='UK'):
    #     return {
    #         'first_name': first_name,
    #         'last_name': last_name,
    #         'age': age,
    #         'city': city,
    #         'country': country
    #     }
    #
    # person = create_person('John', 'Doe', city='New York', country='USA')
    # print(person)
    # # {'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'city': 'New York', 'country': 'USA'}
    #
    # print(create_person(first_name='Anna', last_name='Brown'))
    # # {'first_name': 'Anna', 'last_name': 'Brown', 'age': 18, 'city': 'London', 'country': 'UK'}
    # In this example, the function create_person takes five parameters: first_name, last_name, age, city, and country. The parameters age, city, and country have default values of 18, 'London', and 'UK', respectively. The function call create_person('John', 'Doe', city='New York', country='USA') uses keyword arguments to specify the values for the first_name, last_name, city, and country parameters, while using the default value for the age parameter. This makes it easy to understand what values are being passed to the function and helps to keep the code readable and maintainable.
    #
    # Variable-length Arguments in Python
    # In Python, sometimes, we may not know the number of arguments that will be passed to a function. In such cases, we can use variable-length arguments. There are two types of variable-length arguments: *args and **kwargs.
    #
    # *args
    # *args is a special syntax in Python that allows us to pass a variable number of positional arguments to a function. The syntax to define a function with *args is as follows:
    #
    # def function_name(*args):
    #     # function body
    # Consider the following example of a function that calculates the sum of an arbitrary number of numbers:
    #
    # def add(*args):
    #     res = 0
    #     for number in args:
    #         res += number
    #     return res
    #
    # print(add(1, 2, 3, 4, 5)) # 15
    # In this example, the function add takes a variable number of positional arguments, which are collected into the tuple args. The function call add(1, 2, 3, 4, 5) passes five arguments, and the function returns the expected result.
    #
    # **kwargs
    # **kwargs is a special syntax in Python that allows us to pass a variable number of keyword arguments to a function. The syntax to define a function with **kwargs is as follows:
    #
    # def function_name(**kwargs):
    #     # function body
    # Consider the following example of a function that calculates the product of an arbitrary number of numbers:
    #
    # def product(**kwargs):
    #     result = 1
    #     for key, value in kwargs.items():
    #         result *= value
    #     return result
    #
    # print(product(a = 2, b = 3, c = 4))   # 24
    # In this example, the function product takes a variable number of keyword arguments, which are collected into the dictionary kwargs. The function call product(a = 2, b = 3, c = 4) passes three keyword arguments, and the function returns the expected result.
    #
    # Nuances of Working With Functions
    # It is important to keep in mind a few nuances when working with default arguments in Python. First, default arguments are evaluated only once, at the time of function definition. This means that if you use a mutable object, such as a list or a dictionary, as a default argument, its value will persist between function calls, leading to unexpected results:
    #
    # def add_number(number, numbers=[]):
    #     numbers.append(number)
    #     return numbers
    #
    # print(add_number(1)) # [1]
    # print(add_number(2)) # [1, 2]
    # To avoid this issue, you can use None as the default value, and check for it in the function body:
    #
    # def add_number(number, numbers=None):
    #     if numbers is None:
    #         numbers = []
    #     numbers.append(number)
    #     return numbers
    #
    # print(add_number(1)) # [1]
    # print(add_number(2)) # [2]
    # Another nuance to keep in mind is that positional arguments must be passed before keyword arguments, and those keyword arguments must follow the order of the function definition:
    #
    # def greeting(name, title='Mr.'):
    #     return f'Hello, {title} {name}'
    #
    #
    # print(greeting('John', title='Dr.'))   # Hello, Dr. John
    # print(greeting(title='Dr.', 'John'))   # SyntaxError: positional argument follows keyword argument
    # print(greeting('John', title='Dr.'))   # Hello, Dr. John
    # print(greeting(title='Dr.', 'John'))   # SyntaxError: positional argument follows keyword argument

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Functions_18_ ()
#endif

#endmodule
