#------------------------------------------
# Lists_list02_lists_01 ():
#------------------------------------------
def Lists_list02_lists_01 ():
    """Lists_list02_lists_01"""
#beginfunction
    global list

    print (f'#-----------------------------')
    print (f'# {Lists_list02_lists_01.__name__}')
    print (f'#-----------------------------')

    # Списки Python - упорядоченная, изменяемая коллекция объектов разных типов

    #------------------------------------------
    # How to Create a List?
    # There are many ways of creating and initializing lists.
    # You can use square brackets[] or list(iterable) constructor as shown below
    #------------------------------------------
    # empty list with square brackets
    empty_list = [] # Пустой список
    print (empty_list)
    # empty list with square brackets
    empty_list = list()
    print (empty_list)
    # list of integers
    integer_list = [1, 2, 3]
    print (integer_list)
    # list with mixed data types
    mixed_list = [8, "Hi", 3.3]
    print (mixed_list)
    # list from an iterable object
    iterable_list = list("data-science")
    print (iterable_list)
    # a nested list
    nested_list = ["cat", [3, 2], ['d']]
    print (nested_list)
    # Создать список
    list = list('список')
    print(list)
    # Генератор списков - способ построить новый список, применяя выражение к
    # каждому элементу последовательности
    list = [list * 3 for list in 'list']
    print (list)
    list = [list * 3 for list in 'list' if list != 'i']
    print (list)

    # Python Sequence Functions and Methods

    # Lists support sequence operations like Indexing, Slicing, Membership, Concatenation, Length, Iteration and some others as they are sequence type objects.

    # Indexing: Items in a list can be accessed by index using the indexing operator. Python indexing starts from zero. You can use a negative integer as an index to start from the end. If you use an integer beyond the length of the list then you get IndexError. If your index is not an integer then you get TypeError.
    # list of integers
    integer_list = [1, 2, 3, 4, 5, 6, 7]
    # indexing
    print(integer_list[0]) #prints '1'
    print(integer_list[6]) #prints '7'
    print(integer_list[-1]) #prints '7'
    print(integer_list[-7]) #prints '1'
    print(integer_list['a']) #TypeError: list indices must be integers
    print(integer_list[7]) #IndexError: index is out of range

    # Slicing: Slicing is a very powerful tool as it helps you to create another list with a range of objects contained in the original list. Slicing seems unintuitive at first but once you grasp the basics you can use them easily to enhance the lists operations.
    # list of integers
    integer_list = [1, 2, 3, 4, 5, 6, 7]
    # slicing with [start:end] takes all elements between 'start' to 'end' does not include 'end' element
    print (integer_list [1:3])  # prints '[2, 3]'
    # slicing with [start:] includes all elements after 'start' including the 'start'th  element
    print (integer_list [2:])  # prints [3, 4, 5, 6, 7]
    # slicing with [:ends] includes all elements before 'end' and does not include the 'end'th element
    print (integer_list [:5])  # prints [1, 2, 3, 4, 5]
    # slicing with negative integers to start indexing from end
    print (integer_list [-2:])  # prints [6, 7]
    print (integer_list [:-5])  # prints [1, 2]

    # Membership: You can check whether if a specific object is member of a list or not. To do this, you can use ‘in’ or ‘not in’ membership operators.
    # list of integers
    integer_list = [1, 2, 3, 4, 5, 6, 7]
    # membership
    # 4 in integer_list  # True
    # 8 in integer_list  # False
    # 4 not in integer_list  # False
    # 8 not in integer_list  # True

    # Concatenation: You can use ‘+’ or ‘*’ operators to concatenate the lists.
    # list of integers
    integer_list = [1, 2, 3]
    # list of strings
    string_list = ['data', 'science', 'rocks']
    integer_list + string_list  #[1, 2, 3, 'data', 'science', 'rocks']
    string_list * 2  #['data', 'science', 'rocks', 'data', 'science', 'rocks']

    # Length: If you pass a list to the ‘len()’ function, you will get the length of the list in return.
    # list of integers
    integer_list = [1, 2, 3, 4, 5, 6, 7]
    # len() with lists
    len (integer_list)  # 7

    # Iteration: Lists are iterable objects so you can iterate over a list with for loops.
    # list of integers
    integer_list = [1, 2, 3]
    # iterate over list elements
    for element in integer_list:
        print (element)  # 1 2 3

    # Other operations: There are some additional operations that apply to most of the sequences such as max(), min(), count(), index(). Let’s see how you can use them with list objects;
    # list of integers
    integer_list = [1, 2, 3, 1, 8, 1]
    # max(), min()
    max (integer_list)  # 8
    min (integer_list)  # 1
    # count(), index()
    integer_list.index (3)  # 2
    integer_list.index (1)  # 0
    integer_list.count (1)  # 3
    integer_list.count (9)  # 0



    # List Methods
    # Here are the remaining methods you can use with the list-objects.

    # append(element): Adds a single element to the end of the list. This method modifies the original list and does not return a new list;
    # list of integers
    integer_list = [1, 2, 3]
    # append()
    integer_list.append (5)
    print (integer_list)
    # output
    # [1, 2, 3, 5]

    # extend(other_list): Adds the elements in other_list to the end of the original list;
    integer_list = [1, 2, 3]
    string_list = ['data', 'science']
    # extend()
    integer_list.extend (string_list)  #[1, 2, 3, 'data', 'science']
    integer_list.extend ('rocks')  #[1, 2, 3, 'data', 'science', 'r', 'o', 'c', 'k', 's']

    # insert(index, element): Inserts a single element at the given index and shifts the elements after to the right.
    string_list = ['data', 'science']
    # insert()
    string_list.insert (1, '-')  #['data', '-', 'science']
    string_list.insert (3, 'rocks')  #['data', '-', 'science', 'rocks']

    # sort(key=None, reverse=False) — Sorts the given list, does not return a new list object. sort() function sort the list in ascending order. You can provide reverser = True if you need to sort the list in descending order. You can also define a custom sorting order by creating a function to define which element of list items to be used as a key for ordering. As you can see in the below example, second_char(string_element) function returns the second character of each string element in the original list. The list then sorted based on the return value of the second_char function.
    integer_list = [1, 2, 3, 1, 8, 1]
    # sort()
    integer_list.sort ()
    print (integer_list)
    integer_list.sort (reverse = True)
    print (integer_list)
    # custom sort
    string_list = ['science', 'rocks', 'data']

    def second_char (string_element):
        return string_element [1]

    string_list.sort (key = second_char, reverse = False)
    print (string_list)

    # reverse() — Reverse simply reverse the list order. This function does not return a new list.

    # remove(element): Finds the first instance of the given element and removes it. Throws ValueError, if the given element is not present.

    integer_list = [1, 2, 3, 1, 8, 1]
    # remove()
    integer_list.remove (1)
    print (integer_list)  #[2, 3, 1, 8, 1]
    integer_list.remove (1)
    print (integer_list)  #[2, 3, 8, 1]
    integer_list.remove (2)
    print (integer_list)  #[3, 8, 1]
    integer_list.remove (9)  #ValueError: list.remove(x): x not in list

    # pop(index): Removes and returns the element at the given index. Removes and returns the last element if the index is no provided.
    integer_list = [1, 2, 3, 4, 5, 6, 7]
    # pop()
    integer_list.pop (3)  #returns 4
    print (integer_list)  #[1, 2, 3, 5, 6, 7]
    integer_list.pop ()  #returns 7
    print (integer_list)  #[1, 2, 3, 5, 6]

    # List Comprehensions
    # List comprehensions provide an elegant and concise way of creating lists. The syntax for the list comprehensions;
    new_list = [expression for member in iterable ( if conditional)]
    integer_list = [x for x in range (10) if x % 2 == 0 if x % 5 == 0]
    print (integer_list)  #[0, 10, 20, 30]

    # Conclusion and Key Takeaways
    # As data structures are fundamental parts of our programs, it is really important to have a solid understanding of Python lists to create efficient programs.
    #
    # I explained why and when to use the lists, some of the key takeaways are listed below;
    #
    # Fundamental characteristics of Python lists are as follows; They are mutable, ordered, dynamic and array type (sequence) data structures.
    # We can use the lists when we want to store a collection of heterogeneous objects in a single data structure.
    # New elements can be added or removed in runtime. Lists are not fixed-size objects, so they are called dynamic data structures.
    # The order in which you specify the elements when you define a list is maintained so lists are ordered.


















    # Обращение к элементу списка
    list = [1, 2, 3, 'word']
    print (list)
    print (list[3])
    print (list[-1])

    # Метод или Функция
    # Методы и функции по работе со списками

    # list.append(x)
    #  append(item): добавляет элемент item в конец списка
    #   Добавляет элемент в конец списка

    # list.extend(L)
    #   Расширяет список list, добавляя в конец все элементы списка L

    # list.insert(i, x)
    #  insert(index, item): добавляет элемент item в список по индексу index
    #   Вставляет на i-ый элемент значение x

    # list.remove(x)
    #  remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
    #   Удаляет первый элемент в списке, имеющий значение x.
    #   ValueError, если такого элемента не существует

    # list.pop([i])
    #  pop([index]): удаляет и возвращает элемент по индексу index. Если индексне передан, то просто удаляет последний элемент.
    #   Удаляет i-ый элемент и возвращает его.
    #   Если индекс не указан, удаляется последний элемент


    # list.index(x, [start [, end]])
    #  index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
    #   Возвращает положение первого элемента со значением x
    #   (при этом поиск ведется от start до    end)

    # list.count(x)
    #  count(item): возвращает количество вхождений элемента item в список
    #   Возвращает количество элементов со значением x

    # list.sort([key=функция])
    #  sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию.Но с помощью параметра key мы можем передать функцию сортировки.
    #   Сортирует список на основе функции

    # list.reverse()
    #  reverse(): расставляет все элементы в списке в обратном порядке
    #   Меняет порядок элементов в списке на противоположный

    # list.copy()
    #   Поверхностная копия списка

    # list.clear()
    #  clear(): удаление всех элементов из списка
    #   Очищает список




    # Кроме того, Python предоставляет ряд встроенных функций для работы со списками:

    # max(list)
    #  max(list): возвращает наибольший элемент списка
    #   Максимальное значение в списке

    # min(list)
    #  min(list): возвращает наименьший элемент списка
    #   Минимальное значение в списке

    # sum(list)
    #   Сумма значений в списке

    # sorted(list, reverse=True)
    #  sorted(list,[key]): возвращает отсортированный список
    #   Сортирует список

    # del list[i]
    #   Удаляет i элемент из списка

    #  len(list): возвращает длину списка

#endfunction


#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Lists_list02_lists_01 ()
#endif

#endmodule
