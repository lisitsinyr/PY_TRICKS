#------------------------------------------
# Lists_list02_lists ():
#------------------------------------------
def Lists_list02_lists ():
    """Lists_list02_lists"""
#beginfunction
    global list
    print (f'#-----------------------------')
    print (f'# {Lists_list02_lists.__name__}')
    print (f'#-----------------------------')

    # Клонирование или копирование списка

    # Скопируйте или клонируйте список, используя технику нарезки

    # Это самый простой и быстрый способ клонирования списка. Этот метод используется, когда мы хотим изменить список, а также сохранить копию оригинала. В этом мы создаем копию самого списка вместе со ссылкой. Этот процесс также называется клонированием. Этот метод занимает около 0,039 секунды и является самым быстрым методом
    # Python program to copy or clone a list
    # Using the Slice Operator
    def Cloning (li1):
        li_copy = li1 [:]
        return li_copy
    # Driver Code
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = Cloning (li1)
    print ("Original List:", li1)
    print ("After Cloning:", li2)
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]
    # Временная сложность: O(n), где n - длина фрагмента
    # Вспомогательный пробел: O(1)

    # Клонировать или копировать с помощью метода Python extend()
    # Списки могут быть скопированы в новый список с помощью функции extend() . При этом каждый элемент повторяющегося объекта (например, другой список) добавляется в конец нового списка. Это занимает около 0,053 секунды. В этом примере мы используем extend() для копирования или клонирования списка.

    # Python code to clone or copy a list
    # Using the in-built function extend()
    def Cloning(li1):
        li_copy = []
        li_copy.extend(li1)
        return li_copy


    # Driver Code
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = Cloning(li1)
    print("Original List:", li1)
    print("After Cloning:", li2)
    # Output
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]

    # Python Copy List Using Assignment Operator

    # This is the simplest method of cloning a list by using = operators. This operator assigns the old list to the new list using Python operators. Here we will create a list and then we will copy the old list into the new list using assignment operators. In this example, we are using assignment operator to clone or copy Python list.
    # Python code to clone or copy a list
    # Using the List copy using =
    def Cloning(li1):
        li_copy = li1
        return li_copy

    # Driver Code
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = Cloning(li1)
    print("Original List:", li1)
    print("After Cloning:", li2)
    # Output:
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]
    # Time Complexity: O(1)
    # Auxiliary Space: O(n), where n is length of list.

    # Using Shallow Copy in Python
    # This method of copying using copy. This takes around 0.186 seconds to complete. In this example, we are using Shallow Copy to copy or clone a list in Python.
    # importing copy module
    import copy

    # initializing list 1
    li1 = [1, 2, [3,5], 4]

    # using copy for shallow copy
    li2 = copy.copy(li1)

    print(li2)
    # Output:
    # [1, 2, [3, 5], 4]

    # Python Cloning or Copying a list Using List Comprehension
    # In this example, we are using list comprehension to clone or copy a list.
    # Python code to clone or copy a list
    # Using list comprehension
    def Cloning(li1):
        li_copy = [i for i in li1]
        return li_copy

    # Driver Code
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = Cloning(li1)
    print("Original List:", li1)
    print("After Cloning:", li2)
    # Output:
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]

    # Python append() to Clone or Copy a list
    # This can be used for appending and adding elements to list or copying them to a new list. It is used to add elements to the last position of the list. This takes around 0.325 seconds to complete and is the slowest method of cloning. In this example, we are using Python append to copy a Python list.
    # Python code to clone or copy a list
    # Using append()
    def Cloning(li1):
        li_copy =[]
        for item in li1: li_copy.append(item)
        return li_copy

    # Driver Code
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = Cloning(li1)
    print("Original List:", li1)
    print("After Cloning:", li2)
    # Output:
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]

    # Using the copy() method
    # The Python List copy() is an inbuilt method copy used to copy all the elements from one list to another. This takes around 1.488 seconds to complete.
    # Python code to clone or copy a list
    # Using built-in method copy()
    def Cloning(li1):
        li_copy =[]
        li_copy = li1.copy()
        return li_copy

    # Driver Code
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = Cloning(li1)
    print("Original List:", li1)
    print("After Cloning:", li2)
    # Output:
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]

    # Using the method of Deep Copy
    # This method of copying is well explained in the article Deep Copy. This takes around 10.59 seconds to complete and is the slowest method of cloning.

    # importing copy module
    import copy

    # initializing list 1
    li1 = [1, 2, [3,5], 4]

    # using deepcopy for deepcopy
    li3 = copy.deepcopy(li1)
    print(li3)
    # Output:
    # [1, 2, [3, 5], 4]

    # Copy a List Using Enumerate Function
    # In this example, we are using enumerate function to copy or clone a list.
    # Python code to clone or copy a list
    # Using list comprehension
    lst = [4, 8, 2, 10, 15, 18]
    li_copy = [i for a,i in enumerate(lst)]
    print("Original List:", lst)
    print("After Cloning:", li_copy)
    # Output
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]

    # Python Copy or Clone a List using Map Function
    # In this example, we are using map function to clone or copy a list using map function.
    # Python code to clone or copy a list
    # Using map function
    lst = [4, 8, 2, 10, 15, 18]
    li_copy = map(int, lst)
    print("Original List:", lst)
    print("After Cloning:", *li_copy)
    # Output:
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: 4 8 2 10 15 18

    # Using slice() function
    # The Python slice() is an inbuilt method used to copy all the elements from one list to another. Here slice() function is passed with one argument which is an integer specifying at which position slicing will end.
    # Python code to clone or copy a list
    # Using slice() function
    lst = [4, 8, 2, 10, 15, 18]
    li_copy = lst[slice(len(lst))]
    print("Original List:", lst)
    print("After Cloning:", li_copy)
    # This code is contributed by Pushpesh Raj.
    # Output
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]

    # Using the deque() function
    # The deque() function is used to create a double-ended queue in Python. It can be used to efficiently append or remove elements from both ends of the queue. In this approach, we create a deque object with the original list and then convert it back to a list to create a copy of the original list.
    from collections import deque

    original_list = [4, 8, 2, 10, 15, 18]

    copied_list = deque(original_list)
    copied_list = list(copied_list)

    print("Original List:", original_list)

    print("After Cloning:", copied_list)
    # Output
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]

    # Copy a Python List Using reduce()
    # In this example, we are using reduce() method to copy a list.
    from functools import reduce

    def clone_list(li1):
        return reduce(lambda x, y: x + [y], li1, [])

    # Driver Code
    li1 = [4, 8, 2, 10, 15, 18]
    li2 = clone_list(li1)
    print("Original List:", li1)
    print("After Cloning:", li2)
    #This code is contributed by Jyothi pinjala.
    # Output
    # Original List: [4, 8, 2, 10, 15, 18]
    # After Cloning: [4, 8, 2, 10, 15, 18]
    # Time complexity : O(n), where n is the length of the input list.
    # Space complexity : O(n)


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Lists_list02_lists ()
#endif

#endmodule
