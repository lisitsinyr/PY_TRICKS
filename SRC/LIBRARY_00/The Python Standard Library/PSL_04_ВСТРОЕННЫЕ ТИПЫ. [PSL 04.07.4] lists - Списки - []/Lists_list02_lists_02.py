#------------------------------------------
# Lists_list02_lists_02 ():
#------------------------------------------
def Lists_list02_lists_02 ():
    """Lists_list02_lists_02"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Lists_list02_lists_02.__name__}')
    print (f'#-----------------------------')

    # Python lists are a versatile data type that can hold a collection of elements of any type. Before exploring the powerful list methods in Python, it is important to understand the basic operations that can be performed on lists. In this section, we will cover three essential list operations: creating a list, accessing elements of a list, and slicing a list.
    # Lists can contain any data type, including other lists, and can be created empty or with initial values. Once a list is created, elements can be added, removed, or modified as needed.

    #--------------------------------------
    # Basic List Operations
    # By understanding these basic list operations, you can create, access, and manipulate Python lists with ease. Next, we will explore the powerful list methods that Python offers for even more advanced list manipulation.
    #--------------------------------------

    #--------------------------------------
    # Creating a list
    # To create a list in Python, simply enclose a sequence of comma-separated values inside square brackets. For example:
    #--------------------------------------
    fruits = ['apple', 'banana', 'cherry', 'durian']
    numbers = [1, 2, 3, 4, 5]
    mixed_list = [1, 'apple', True, 3.14]

    #--------------------------------------
    # Accessing elements of a list
    # To access an element of a list, use the index of the element inside square brackets. The index of the first element of a list is 0, and the index of the last element is len(list)-1. For example:
    #--------------------------------------
    fruits = ['apple', 'banana', 'cherry', 'durian']
    print(fruits[0]) # Output: 'apple'
    print(fruits[2]) # Output: 'cherry'
    print(fruits[-1]) # Output: 'durian'
    # Negative indices count from the end of the list. Therefore, fruits[-1] returns the last element of the list, ‘durian’.

    #--------------------------------------
    # Slicing a list
    # Slicing a list means extracting a subset of the elements in the list. To slice a list, use the colon operator (:) inside square brackets to specify the start and end indices of the slice. For example:
    #--------------------------------------
    numbers = [1, 2, 3, 4, 5]
    print(numbers[1:4]) # Output: [2, 3, 4]
    print(numbers[:3]) # Output: [1, 2, 3]
    print(numbers[2:]) # Output: [3, 4, 5]
    # In the first example, numbers[1:4] returns the slice of the list starting at index 1 and ending at index 3 (not including index 4). In the second example, numbers[:3] returns the slice of the list starting at the beginning and ending at index 2 (not including index 3). In the third example, numbers[2:] returns the slice of the list starting at index 2 and ending at the end of the list.


    #--------------------------------------
    # Powerful List Methods
    #--------------------------------------

    #--------------------------------------
    # append()
    # The append() method adds an element to the end of a list. It takes a single argument, which is the value to be added. For example, let’s say we have a list of numbers as follows:
    #--------------------------------------
    numbers = [1, 2, 3, 4]
    # To add a new number to the end of the list, we can use the append() method:
    numbers.append(5)
    print(numbers) # Output: [1, 2, 3, 4, 5]

    #--------------------------------------
    # extend()
    # The extend() method adds the elements of another list to the end of the current list. It takes a single argument, which is the list of elements to be added. For example:
    #--------------------------------------
    fruits = ['apple', 'banana', 'cherry']
    more_fruits = ['orange', 'grape']
    fruits.extend(more_fruits)
    print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange', 'grape']

    #--------------------------------------
    # insert()
    # The insert() method adds an element to a specific index in the list. It takes two arguments: the index where the element will be inserted and the value to be inserted. For example:
    #--------------------------------------
    letters = ['a', 'b', 'c', 'd']
    letters.insert(2, 'e')
    print(letters) # Output: ['a', 'b', 'e', 'c', 'd']

    #--------------------------------------
    # remove()
    # The remove() method removes the first occurrence of a specified element in the list. It takes a single argument, which is the element to be removed. For example:
    #--------------------------------------
    numbers = [1, 2, 3, 4, 5]
    numbers.remove(3)
    print(numbers) # Output: [1, 2, 4, 5]

    #--------------------------------------
    # pop()
    # The pop() method removes the element at a specified index in the list and returns it. If no index is specified, it removes and returns the last element in the list. For example:
    #--------------------------------------
    letters = ['a', 'b', 'c', 'd']
    x = letters.pop(1)
    print(x) # Output: 'b'
    print(letters) # Output: ['a', 'c', 'd']

    #--------------------------------------
    # sort()
    # The sort() method sorts the elements in the list in ascending order by default. It can also sort the list in descending order by specifying the reverse parameter as True. For example:
    #--------------------------------------
    numbers = [5, 2, 1, 3, 4]
    numbers.sort()
    print(numbers) # Output: [1, 2, 3, 4, 5]
    numbers.sort(reverse=True)
    print(numbers) # Output: [5, 4, 3, 2, 1]

    #--------------------------------------
    # count()
    # The count() method returns the number of times a specified element appears in the list. It takes a single argument, which is the element to be counted. For example:
    #--------------------------------------
    fruits = ['apple', 'banana', 'cherry', 'banana']
    x = fruits.count('banana')
    print(x) # Output:

    #--------------------------------------
    # index()
    # The index() method returns the index of the first occurrence of a specified element in the list. It takes a single argument, which is the element to be searched. For example:
    #--------------------------------------
    numbers = [1, 2, 3, 4, 5]
    x = numbers.index(3)
    print(x) # Output: 2

    #--------------------------------------
    # Examples of Using List Methods in Python
    # Python lists provide a wide range of built-in methods for manipulating list elements. In this section, we will explore some examples of how to use these methods to perform common tasks, including adding and removing elements from a list, sorting a list, finding elements in a list, and concatenating two or more lists.
    #--------------------------------------

    # Adding and removing elements from a list
    # The append() method adds an element to the end of a list, while the insert() method inserts an element at a specified position. For example:
    fruits = ['apple', 'banana', 'cherry']
    fruits.append('durian')
    print(fruits) # Output: ['apple', 'banana', 'cherry', 'durian']
    fruits.insert(1, 'orange')
    print(fruits) # Output: ['apple', 'orange', 'banana', 'cherry', 'durian']
    fruits.remove('banana')
    print(fruits) # Output: ['apple', 'orange', 'cherry', 'durian']
    fruits.pop()
    print(fruits) # Output: ['apple', 'orange', 'cherry']
    # The remove() method removes the first occurrence of the specified element from the list, while the pop() method removes and returns the last element of the list.

    #--------------------------------------
    # Sorting a list
    # The sort() method sorts the elements of a list in ascending order by default. For example:
    #--------------------------------------
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    numbers.sort()
    print(numbers) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    fruits = ['apple', 'banana', 'cherry', 'durian']
    fruits.sort()
    print(fruits) # Output: ['apple', 'banana', 'cherry', 'durian']
    # The sort() method can also sort in descending order by passing the reverse=True parameter.

    #--------------------------------------
    # Finding elements in a list
    # The count() method returns the number of occurrences of a specified element in a list, while the index() method returns the index of the first occurrence of the specified element. For example:
    #--------------------------------------
    numbers = [1, 2, 3, 4, 5, 5, 5]
    print(numbers.count(5)) # Output: 3
    fruits = ['apple', 'banana', 'cherry']
    print(fruits.index('banana')) # Output: 1

    #--------------------------------------
    # Concatenating two or more lists
    # The extend() method adds the elements of one list to the end of another list. For example:
    #--------------------------------------
    fruits = ['apple', 'banana']
    more_fruits = ['cherry', 'durian']
    fruits.extend(more_fruits)
    print(fruits) # Output: ['apple', 'banana', 'cherry', 'durian']
    # By mastering these list methods, you can perform powerful operations on lists and write efficient Python programs.

    #--------------------------------------
    # Best Practices for Using List Methods
    # While Python list methods are powerful and flexible, there are some best practices to follow when using them to write efficient, readable, and maintainable code. Here are some tips to keep in mind:
    #--------------------------------------

    #--------------------------------------
    # Use List Comprehensions
    # Use list comprehensions instead of loops for simple operations. List comprehensions are concise and efficient ways to create lists based on existing lists, while loops can be slower and harder to read. For example, instead of using a loop to square the elements of a list:
    #--------------------------------------
    numbers = [1, 2, 3, 4, 5]
    squares = []
    for number in numbers:
        squares.append(number**2)
    # You can use a list comprehension:
    numbers = [1, 2, 3, 4, 5]
    squares = [number**2 for number in numbers]

    #--------------------------------------
    # Use List Slicing
    # Use slicing to create copies of lists. When you need to create a copy of a list, slicing is a more efficient and readable alternative to using the copy() method. For example, instead of:
    #--------------------------------------
    fruits = ['apple', 'banana', 'cherry']
    copy_fruits = fruits.copy()
    # You can use slicing:
    fruits = ['apple', 'banana', 'cherry']
    copy_fruits = fruits[:]

    #--------------------------------------
    # Use “in” Keyword
    # Use the in keyword to check if an element is in a list. The in keyword is a more efficient and readable alternative to using the count() or index() methods to check if an element is in a list. For example, instead of:
    #--------------------------------------
    fruits = ['apple', 'banana', 'cherry']
    if fruits.count('banana') > 0:
        print('Found banana!')
    # You can use the in keyword:

    fruits = ['apple', 'banana', 'cherry']
    if 'banana' in fruits:
        print('Found banana!')

    #--------------------------------------
    # Use Descriptive Variable Names
    # Use descriptive variable names to make your code more readable. Instead of using generic variable names like a or b, use descriptive names that indicate the purpose of the variable. For example:
    #--------------------------------------
    students = ['Alice', 'Bob', 'Charlie']
    student_names = [name.lower() for name in students]

    #--------------------------------------
    # Keep your Code DRY
    # Keep your code DRY (Don’t Repeat Yourself) by using variables and functions to avoid repetition. For example, instead of repeating the same list operation multiple times:
    #--------------------------------------
    fruits = ['apple', 'banana', 'cherry']
    print(fruits[0])
    print(fruits[1])
    print(fruits[2])
    # You can use a loop or a function:
    fruits = ['apple', 'banana', 'cherry']
    for fruit in fruits:
        print(fruit)
    def print_list_elements(lst):
        for element in lst:
            print(element)
    print_list_elements(fruits)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Lists_list02_lists_02 ()
#endif

#endmodule
