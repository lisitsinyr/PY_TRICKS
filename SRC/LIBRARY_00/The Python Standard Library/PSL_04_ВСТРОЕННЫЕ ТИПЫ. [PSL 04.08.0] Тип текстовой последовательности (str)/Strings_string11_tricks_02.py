#------------------------------------------
# Strings_string11_tricks_02 ():
#------------------------------------------
def Strings_string11_tricks_02 ():
    """Strings_string11_tricks_02"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string11_tricks_02.__name__}')
    print (f'#-----------------------------')

    # Link: https://t.me/pythonercode/2208
    #
    # Дата: 2025-06-27 17:22:45+00:00
    #
    # Title: Pythoner
    #
    # ➡️**В Python существует концепция "сырых строк" (raw
    # strings), которая позволяет обозначить строку таким образом,
    # чтобы все символы в ней интерпретировались буквально, без
    # учета экранирующих символов (escape characters). **
    #
    # ➡️В сырой строке символ обратного слэша '\' не будет
    # интерпретироваться как начало экранированной
    # последовательности, а будет рассматриваться просто как
    # обычный символ.
    #
    # ➡️Это особенно удобно, например, при работе с путями к
    # файлам в операционной системе Windows, где обратные слеши
    # используются для разделения директорий, но могут мешать при
    # использовании обычных строк из-за экранирования.
    #
    # **💡****Заключение**
    # Таким образом, сырые строки позволяют избежать необходимости
    # использования двойных обратных слешей при работе с путями
    # файлов, что делает код более читаемым и удобным для работы.





    # https://bobbyhadz.com/blog/all-in-programming
    # https://bobbyhadz.com

    # ---------------------------------------------------
    # Remove Backslashes or Forward slashes from String in Python
    # ---------------------------------------------------
    # 1.Remove backslashes from a String in Python
    # 2.Remove forward slash from a String in Python
    # 3.Remove the trailing Slash from a String in Python
    # 4.Remove leading and trailing Slash from String in Python
    # 5.Replace double backslash with single backslash in Python
    # 6.Replace single backslash with double backslash in Python
    # ---------------------------------------------------

    # ---------------------------------------------------
    # 1.Remove backslashes from a String in Python #
    # ---------------------------------------------------
    # Use the str.replace() method to remove the backslashes from a string, e.g. string.replace('\\', '').
    # The str.replace() method will remove the backslashes from the string by replacing them with empty strings.
    # ---------------------------------------------------
    string = '\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \bobby\hadz\com\
    # ✅ Remove all backslashes from a string
    new_string = string.replace('\\', '')
    print(new_string)  # 👉️ bobbyhadzcom

    # ---------------------------------------------------
    # ✅ Remove first occurrence of backslash from a string
    # ---------------------------------------------------
    new_string = string.replace('\\', '', 1)
    print(new_string)  # 👉️ bobby\hadz\com\
    # We used the str.replace() method to remove the backslashes from a string.

    # The backslash \ character has a special meaning in Python - it is used as an escape character (e.g. \n or \t).
    # By adding a second backslash, we treat the backslash (\) as a literal character.
    my_str = 'bobby \\ hadz'
    print(my_str)  # 👉️ bobby \ hadz
    # The str.replace method returns a copy of the string with all occurrences of a substring replaced by the provided replacement.
    #
    # The method takes the following parameters:
    #
    # Name  Description
    # old   The substring we want to replace in the string
    # new   The replacement for each occurrence of old
    # count Only the first count occurrences are replaced (optional)
    # The method doesn't change the original string. Strings are immutable in Python.
    #
    # If you don't need to keep the original string around, reassign the variable rather than declaring a new one.
    string = '\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \bobby\hadz\com\
    #
    string = string.replace('\\', '')
    print(string)  # 👉️ bobbyhadzcom
    # If you only need to remove the first backslash character from the string, set the count argument to 1 in the call to str.replace().
    #
    string = '\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \bobby\hadz\com\
    #
    new_string = string.replace('\\', '', 1)
    print(new_string)  # 👉️ bobby\hadz\com\
    # When the count argument is set, only the first count occurrences are replaced.
    #
    # If you only need to remove the leading and trailing backslashes from a string, use the str.strip() method.
    #
    string = '\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \bobby\hadz\com\
    #
    new_string = string.strip('\\')
    print(new_string) # 👉️ bobby\hadz\com
    # The str.strip method returns a copy of the string with the specified leading and trailing characters removed.

    # If you only need to remove the leading or trailing backslashes from a string, use the str.lstrip() or str.rstrip() method.
    string = '\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \bobby\hadz\com\
    # ✅ Remove leading backslashes from a string
    new_string = string.lstrip('\\')
    print(new_string) # 👉️ bobby\hadz\com\
    # ✅ Remove trailing backslashes from a string
    new_string = string.rstrip('\\')
    print(new_string) # 👉️ \bobby\hadz\com
    # The str.lstrip method takes a string containing characters as an argument and returns a copy of the string with the specified leading characters removed.
    # The str.rstrip method takes a string containing characters as an argument and returns a copy of the string with the specified trailing characters removed.

    # ---------------------------------------------------
    # 2.Remove forward slash from a String in Python #
    # ---------------------------------------------------
    # You can also use the str.replace() method to remove the forward slashes from a string.
    # ---------------------------------------------------
    string = '/bobby/hadz/com/'
    print(string)  # 👉️ \bobby\hadz\com\

    # ✅ Remove forward slashes from string
    new_string = string.replace('/', '')
    print(new_string)  # 👉️ bobbyhadzcom

    # ✅ Remove backslashes from string
    string = '\\bobby\\hadz\\com\\'
    new_string = string.replace('\\', '')
    print(new_string)  # 👉️ bobbyhadzcom
    # The first example removes the forward slashes from a string and the second example removes the backslashes.

    # Backslashes have a special meaning - they are used as an escape character, e.g. \n, so we added a second backslash to treat them as literal characters.
    # To remove the forward slashes from the string, we simply replace each forward slash with an empty string.
    string = '/bobby/hadz/com/'
    print(string)  # 👉️ \bobby\hadz\com\

    new_string = string.replace('/', '')
    print(new_string)  # 👉️ bobbyhadzcom
    # The str.replace method returns a copy of the string with all occurrences of a substring replaced by the provided replacement.

    # The method takes the following parameters:
    # old       The substring we want to replace in the string
    # new       The replacement for each occurrence of old
    # count     Only the first count occurrences are replaced (optional)
    # The method doesn't change the original string. Strings are immutable in Python.

    # If you don't need to keep the original string around, reassign the variable rather than declaring a new one.
    string = '/bobby/hadz/com/'
    print(string)  # 👉️ \bobby\hadz\com\
    string = string.replace('/', '')
    print(string)  # 👉️ bobbyhadzcom

    # If you only need to remove the first forward slash from the string, set the count argument to 1 in the call to str.replace().
    string = '/bobby/hadz/com/'
    print(string)  # 👉️ \bobby\hadz\com\
    string = string.replace('/', '', 1)
    print(string)  # 👉️ bobby/hadz/com/
    # When the count argument is set, only the first count occurrences are replaced.

    # If you only need to remove the leading and trailing forward slashes from a string, use the str.strip() method.
    string = '/bobby/hadz/com/'
    print(string)  # 👉️ \bobby\hadz\com\
    string = string.strip('/')
    print(string)  # 👉️ bobby/hadz/com
    # The str.strip method returns a copy of the string with the specified leading and trailing characters removed.

    # If you only need to remove the leading or trailing forward slashes from a string, use the str.lstrip() or str.rstrip() method.
    string = '/bobby/hadz/com/'
    print(string)  # 👉️ \bobby\hadz\com\
    new_string = string.lstrip('/')
    print(new_string)  # 👉️ bobby/hadz/com/
    new_string = string.rstrip('/')
    print(new_string)  # 👉️ /bobby/hadz/com
    # The str.lstrip method takes a string containing characters as an argument and returns a copy of the string with the specified leading characters removed.
    # The str.rstrip method takes a string containing characters as an argument and returns a copy of the string with the specified trailing characters removed.

    # ---------------------------------------------------
    # 2.Remove the trailing Slash from a String in Python #
    # ---------------------------------------------------
    # Use the str.rstrip() method to remove the trailing slash from a string.
    # ---------------------------------------------------
    string = '/bobby/hadz/com/'
    # ✅ Remove the trailing forward slash from a string
    new_string = string.rstrip('/')
    print(new_string) # 👉️ /bobby/hadz/com
    # ✅ Remove the trailing backslash from a string
    string = '\\bobby\\hadz\\com\\'
    new_string = string.rstrip('\\')
    print(new_string)
    # The str.rstrip() method will return a copy of the string with the trailing slash removed.
    # The first example removes the trailing forward slashes from a string and the second example removes the trailing backslashes.
    # The str.rstrip method takes a string containing characters as an argument and returns a copy of the string with the specified trailing characters removed.
    string = '/bobby/hadz/com/'
    new_string = string.rstrip('/')
    print(new_string) # 👉️ \bobby\hadz\com
    # The method doesn't change the original string, it returns a new string. Strings are immutable in Python.

    # If you don't need to keep the original string around, reassign the variable rather than declaring a new one.
    string = '/bobby/hadz/com/'
    string = string.rstrip('/')
    print(string)  # 👉️ /bobby/hadz/com
    # Note that the str.rstrip() method removes one or more occurrences of the specified character from the end of the string.
    string = '/bobby/hadz/com///'
    string = string.rstrip('/')
    print(string)  # 👉️ /bobby/hadz/com

    # If you need to only remove the last character if it's a slash, use the str.endswith() method.
    # Remove the trailing Slash from a String using string slicing #
    # This is a two-step process:
    # Use the str.endswith() method to check if the string ends with a backslash.
    # If the condition is met, use string slicing to remove the trailing slash.
    string = '/bobby/hadz/com//'
    if string.endswith('/'):
        string = string[:-1]
    print(string) # 👉️ /bobby/hadz/com/
    # We used the str.endswith() method to check if the string ends with a forward slash.

    # You can use the same approach to remove the trailing backslash from a string.
    string = '\\bobby\\hadz\\com\\'
    if string.endswith('\\'):
        string = string[:-1]
    print(string)  # 👉️ \bobby\hadz\com
    # The str.endswith method returns True if the string ends with the provided suffix, otherwise the method returns False.
    # If the condition is met, we use string slicing to remove the last character from the string.
    # The syntax for string slicing is my_str[start:stop:step].
    # The start index is inclusive, whereas the stop index is exclusive (up to, but not including).
    # Python indexes are zero-based, so the first character in a string has an index of 0, and the last character has an index of -1 or len(my_str) - 1.
    # The slice string[:-1] starts at index 0 and goes up to, but not including the last character of the string.

    # ---------------------------------------------------
    # 4.Remove leading and trailing Slash from String in Python #
    # ---------------------------------------------------
    # Use the str.strip() method to remove the leading and trailing slash from a string.
    string = '/bobby/hadz/com/'
    print(string)  # 👉️ /bobby/hadz/com/
    # ✅ Remove leading and trailing forward slash from string
    new_string = string.strip('/')
    print(new_string)  # 👉️ bobby/hadz/com
    # ✅ Remove leading and trailing backslash from string
    string = '\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \bobby\hadz\com\
    new_string = string.strip('\\')
    print(new_string)  # 👉️ bobby\hadz\com
    # The first example removes the leading and trailing forward slashes from a string and the second removes the leading and trailing backslashes.
    # The str.strip method returns a copy of the string with the specified leading and trailing characters removed.
    string = '/bobby/hadz/com/'
    print(string)  # 👉️ /bobby/hadz/com/
    new_string = string.strip('/')
    print(new_string)  # 👉️ bobby/hadz/com
    # The method doesn't change the original string, it returns a new string. Strings are immutable in Python.
    # If you only need to remove the leading or trailing slashes from the string, use the str.lstrip() or str.rstrip() method.
    string = '/bobby/hadz/com/'
    new_string = string.lstrip('/')
    print(new_string)  # 👉️ bobby/hadz/com/
    #
    new_string = string.rstrip('/')
    print(new_string)  # 👉️ /bobby/hadz/com
    # The str.lstrip method takes a string containing characters as an argument and returns a copy of the string with the specified leading characters removed.
    # The str.rstrip method takes a string containing characters as an argument and returns a copy of the string with the specified trailing characters removed.
    # Note that the str.strip(), str.lstrip() and str.rstrip() method remove one or more occurrences of the specified leading and trailing characters.
    string = '///bobby/hadz/com///'
    string = string.strip('/')
    print(string) # 👉️ bobby/hadz/com

    # If you need to only remove the first leading and trailing slash, use the str.startswith() and str.endswith() methods.
    # Remove leading and trailing Slash from String using string slicing #
    # This is a three-step process:
    # Use the str.startswith() method to check if the string starts with a slash.
    # Use the str.endswith() method to check if the string ends with a slash.
    # If the conditions are met, use string slicing to remove the slashes.
    string = '//bobby/hadz/com//'
    print(string)  # 👉️ \bobby\hadz\com\
    if string.startswith('/'):
        string = string[1:]
    if string.endswith('/'):
        string = string[:-1]
    print(string)  # 👉️ /bobby/hadz/com/
    # We used the str.startswith() and str.endswith() methods to check if the string starts with and ends with a slash.
    # The str.startswith method returns True if the string starts with the provided prefix, otherwise the method returns False.
    # The str.endswith method returns True if the string ends with the provided suffix, otherwise the method returns False.
    # If the conditions are met, we use string slicing to remove the first and last characters from the string.
    # The syntax for string slicing is my_str[start:stop:step].
    # The start index is inclusive, whereas the stop index is exclusive (up to, but not including).
    # Python indexes are zero-based, so the first character in a string has an index of 0, and the last character has an index of -1 or len(my_str) - 1.
    # The slice string[1:] starts at index 1 and goes to the end of the string.
    # The slice string[:-1] starts at index 0 and goes up to, but not including the last character of the string.

    # ---------------------------------------------------
    # 5.Replace double backslash with single backslash in Python #
    # ---------------------------------------------------
    # The str.replace() method can also be used to replace double backslash with single backslash.
    string = 'bobby\\\\hadz\\\\com'
    print(string)  # 👉️ bobby\\hadz\\com
    new_string = string.replace('\\\\', '\\')
    print(new_string)  # 👉️ bobby\hadz\com
    string = r'bobby\hadz\com'
    print(string) # 👉️ bobby\hadz\com
    # The backslash \ character has a special meaning in Python - it is used as an escape character (e.g. \n or \t).
    # By adding a second backslash, we treat the backslash (\) as a literal character.
    my_str = 'bobby \\ hadz'
    print(my_str)  # 👉️ bobby \ hadz
    # To have two backslashes next to one another, we have to use four backslash characters.
    my_str = 'bobby \\\\ hadz'
    print(my_str)  # 👉️ bobby \\ hadz
    # The str.replace method returns a copy of the string with all occurrences of a substring replaced by the provided replacement.
    string = 'bobby\\\\hadz\\\\com'
    print(string)  # 👉️ bobby\\hadz\\com
    new_string = string.replace('\\\\', '\\')
    print(new_string)  # 👉️ bobby\hadz\com
    # The method takes the following parameters:
    # old   The substring we want to replace in the string
    # new   The replacement for each occurrence of old
    # count Only the first count occurrences are replaced (optional)
    # The method doesn't change the original string. Strings are immutable in Python.
    # Processing an escape sequence with bytes.decode() #
    # If you need to process an escape sequence, use the bytes.decode() method.
    string = 'bobby\\nhadz'
    new_string = bytes(string, "utf-8").decode("unicode_escape")
    # bobby
    # hadz
    print(new_string)
    # We used the bytes() class to convert the string to a bytes object and then used the bytes.decode() method to decode the bytes object into a string with the unicode_escape encoding.
    # If you have access to the variable that declared the string, you can mark it as a raw string.
    string = r'bobby\hadz\com'
    print(string)  # 👉️ bobby\hadz\com
    string = r'bobby\\hadz\\com'
    print(string)  # 👉️ bobby\\hadz\\com
    # Strings that are prefixed with r are called raw strings and treat backslashes as literal characters.
    # We don't have to escape backslashes in raw strings.
    # If you need to use variables in a raw string, use a formatted string literal.
    variable = 'maybe'
    my_str = fr'yes\no\{variable}'
    print(my_str)  # 👉️ yes\no\maybe
    # Formatted string literals (f-strings) let us include expressions inside of a string by prefixing the string with f.
    # Make sure to wrap expressions in curly braces - {expression}.
    # Notice that we prefixed the string with fr and not just with f.

    # ---------------------------------------------------
    # 6.Replace single backslash with double backslash in Python #
    # ---------------------------------------------------
    # The same approach can be used to replace single with double backslash.
    string = '\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \bobby\hadz\com\
    #
    result = string.replace('\\', '\\\\')
    print(result)  # 👉️ \\bobby\\hadz\\com\\
    # We used the str.replace() method to replace a single backslash with two backslashes.
    #
    # The backslash \ character has a special meaning in Python - it is used as an escape character (e.g. \n or \t).
    # By adding a second backslash, we treat the backslash (\) as a literal character.
    my_str = 'bobby \\ hadz'
    print(my_str)  # 👉️ bobby \ hadz
    # To have two backslashes next to one another, we have to use four backslash characters.
    my_str = 'bobby \\\\ hadz'
    print(my_str)  # 👉️ bobby \\ hadz
    # The str.replace method returns a copy of the string with all occurrences of a substring replaced by the provided replacement.
    string = '\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \bobby\hadz\com\
    #
    result = string.replace('\\', '\\\\')
    print(result)  # 👉️ \\bobby\\hadz\\com\\
    # The method takes the following parameters:
    #
    # Name  Description
    # old   The substring we want to replace in the string
    # new   The replacement for each occurrence of old
    # count Only the first count occurrences are replaced (optional)
    # The method doesn't change the original string. Strings are immutable in Python.
    #
    # If you have access to the variable that declared the string, you can mark it as a raw string.
    string = r'\\bobby\\hadz\\com\\'
    print(string)  # 👉️ \\bobby\\hadz\\com\\
    #
    string = r'C:\Users\BobbyHadz\Desktop\example.txt'
    print(string)  # 👉️ C:\Users\BobbyHadz\Desktop\example.txt
    # Strings that are prefixed with r are called raw strings and treat backslashes as literal characters.
    #
    # We don't have to escape backslashes in raw strings.
    #
    # If you need to use variables in a raw string, use a formatted string literal.
    variable = 'maybe'
    my_str = fr'yes\no\{variable}'
    print(my_str)  # 👉️ yes\no\maybe
    # Formatted string literals (f-strings) let us include expressions inside of a string by prefixing the string with f.
    # Make sure to wrap expressions in curly braces - {expression}.

    # Notice that we prefixed the string with fr and not just with f.

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string11_tricks_02 ()
#endif

#endmodule
