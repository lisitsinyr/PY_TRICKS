#------------------------------------------
# Lambdas_04_ ():
#------------------------------------------
def Lambdas_04_ ():
    """Lambdas_04_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Lambdas_04_.__name__)
    print ('#-----------------------------')

    # Python’s Secret Weapon: Lambda Functions
    # Ryk Kiel
    # Ryk Kiel
    #
    # ·
    # Follow
    #
    # 3 min read
    # ·
    # Jan 28
    #
    #
    #
    #
    # Photo by Nick Fewings on Unsplash
    # Lambda functions, also known as anonymous functions, are a powerful feature in Python that allow you to create small, one-time-use functions without the need to define them using the traditional def keyword. These functions are defined using the lambda keyword, followed by one or more arguments and a single expression.
    #
    # Lambda function
    # A simple example of a lambda function is one that takes two arguments and returns their sum:
    #
    # sum = lambda x, y: x + y
    # print(sum(5, 3)) # Output: 8
    # In this example, lambda x, y: x + y is the lambda function. It takes two arguments, x and y, and returns the sum of these arguments. The function is then assigned to the variable sum, and can be called like any other function.
    #
    # Map with lambda
    # Lambda functions can also be used as arguments to other functions. For example, the map() function can be used to apply a given function to each element of an iterable. Here's an example of using a lambda function with map() to square each element of a list:
    #
    # numbers = [1, 2, 3, 4, 5]
    # squared_numbers = map(lambda x: x**2, numbers)
    # print(list(squared_numbers)) # Output: [1, 4, 9, 16, 25]
    # In this example, the lambda function lambda x: x**2 is passed as the first argument to map(), and the list numbers is passed as the second argument. The function is applied to each element of the list, and the resulting iterable is then converted to a list and printed.
    #
    # Filter with lambda
    # Another common use of lambda functions is with the filter() function, which can be used to filter the elements of an iterable based on a given condition. Here's an example of using a lambda function with filter() to select only even numbers from a list:
    #
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # even_numbers = filter(lambda x: x % 2 == 0, numbers)
    # print(list(even_numbers)) # Output: [2, 4, 6, 8, 10]
    # In this example, the lambda function lambda x: x % 2 == 0 is passed as the first argument to filter(), and the list numbers is passed as the second argument. The function is applied to each element of the list, and only the elements for which the function returns True are included in the resulting iterable.
    #
    # Reduce with lambda
    # Lambda functions can also be used with the reduce() function, which is used to apply a binary function to the elements of an iterable in a cumulative way. Here's an example of using a lambda function with reduce() to calculate the product of all the elements of a list:
    #
    # from functools import reduce
    # numbers = [1, 2, 3, 4, 5]
    # product = reduce(lambda x, y: x*y, numbers)
    # print(product) # Output: 120
    # In this example, the lambda function lambda x, y: x*y is passed as the first argument to reduce(), and the list numbers is passed as the second argument. The function is applied to the first two elements of the list, then to the result and the next element, and so on, until a single result is obtained. In this example, the result is the product of all the elements in the list, which is printed.
    #
    # Final remarks
    # It’s worth noting that lambda functions can only contain a single expression, so they are best suited for simple operations. For more complex operations, it’s generally better to use a regular function defined with the def keyword.
    #
    # In addition to their use as arguments to built-in functions, lambda functions can also be assigned to variables and used as regular functions. This can be useful when you need to pass a function as an argument to another function and don’t want to define a separate function for that purpose.
    #
    # Conclusion
    # In conclusion, lambda functions are a powerful and versatile feature in Python that can help you write more concise and readable code. They are useful for small, one-time-use functions, and can be used as arguments to other functions to perform operations on data. With a little practice and the right use cases, you can become a pro at using lambda functions in Python.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Lambdas_04_ ()
#endif

#endmodule
