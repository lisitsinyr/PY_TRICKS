#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/c/1849804501/600
    # 🛡 Регулярные выражения в python
    #
    # Регулярные выражения (regex) в Python используются для
    # поиска, соответствия и манипулирования строками на основе
    # шаблонов. В Python регулярные выражения реализованы в модуле
    # re. Вот основные функции и примеры их использования:
    #
    # Основные функции модуля re:
    #
    # ⏺re.match(): Проверяет, соответствует ли начало строки
    # заданному шаблону.
    # ⏺re.search(): Ищет шаблон в строке и возвращает первый
    # найденный совпадающий объект.
    # ⏺re.findall(): Находит все совпадения шаблона в строке и
    # возвращает их в виде списка.
    # ⏺re.finditer(): Находит все совпадения шаблона и возвращает
    # их в виде итератора.
    # ⏺re.sub(): Заменяет все совпадения шаблона на заданную
    # строку.
    # ⏺re.split(): Разделяет строку по заданному шаблону.
    #
    # 👩‍💻Примеры использования:
    #
    # import re
    #
    # # Пример строки
    # text = "The rain in Spain falls mainly in the plain."
    #
    # # 1. re.match()
    # match = re.match(r'The', text)
    # if match:
    #     print("Match found:", match.group())
    # else:
    #     print("No match found")
    #
    # # 2. re.search()
    # search = re.search(r'rain', text)
    # if search:
    #     print("Search found:", search.group())
    # else:
    #     print("No search found")
    #
    # # 3. re.findall()
    # findall = re.findall(r'in', text)
    # print("Findall results:", findall)
    #
    # # 4. re.finditer()
    # finditer = re.finditer(r'in', text)
    # for match in finditer:
    #     print("Finditer match:", match.group(), "at position",
    # match.start())
    #
    # # 5. re.sub()
    # substitute = re.sub(r'rain', 'snow', text)
    # print("Substitute result:", substitute)
    #
    # # 6. re.split()
    # split = re.split(r'\s', text)
    # print("Split result:", split)
    # Объяснение примера:
    # ➡️re.match(r'The', text): Проверяет, начинается ли строка
    # text с "The".
    # ➡️re.search(r'rain', text): Ищет первое вхождение "rain" в
    # строке text.
    # ➡️re.findall(r'in', text): Находит все вхождения "in" в
    # строке text.
    # ➡️re.finditer(r'in', text): Возвращает итератор, который
    # перебирает все вхождения "in" в строке text.
    # ➡️re.sub(r'rain', 'snow', text): Заменяет все вхождения
    # "rain" на "snow" в строке text.
    # ➡️re.split(r'\s', text): Разделяет строку text по пробелам
    # (символы пробела).
    #
    # Дополнительные примеры шаблонов:
    #
    # ⏺\d: Любая цифра.
    # ⏺\D: Любой символ, кроме цифры.
    # ⏺\w: Любая буква, цифра или символ подчеркивания.
    # ⏺\W: Любой символ, кроме буквы, цифры или символа
    # подчеркивания.
    # ⏺\s: Любой пробельный символ.
    # ⏺\S: Любой непробельный символ.
    # ⏺.: Любой символ, кроме новой строки.
    # ⏺^: Начало строки.
    # ⏺$: Конец строки.
    # ⏺*: 0 или более повторений.
    # ⏺+: 1 или более повторений.
    # ⏺?: 0 или 1 повторение.
    # ⏺{n}: Ровно n повторений.
    # ⏺{n,}: n или более повторений.
    # ⏺{n,m}: От n до m повторений.
    #
    # Регулярные выражения — мощный инструмент для работы с
    # текстом, и они могут быть полезны в самых разных задачах, от
    # простой проверки ввода до сложного парсинга текста.
    #
    # Cheatograph
    #
    # Special characters
    #
    # Default: Match any character
    # except newline
    #
    # DOTALL: Match any character
    # including newline
    #
    # ‘ Default: Match the start of a string
    #
    # “ MULTILINE: Match immediatly
    # after each newline
    #
    # $ Match the end of a string
    #
    # $ MULTILINE: Also match before a
    # newline
    #
    # : Match 0 or more repetitions of RE
    #
    # + Match 1 or more repetitions of RE
    #
    # a Match 0 or 1 repetitions of RE
    #
    # *2,%+, Match non-greedy as few
    #
    # 227 characters as possible
    #
    # {m} Match exactly m copies of the
    #
    # previous RE
    #
    # (m,n) Match from m to n repetitions of
    # RE
    #
    # {m,n}? Match non-greedy
    #
    # \ Escape special characters
    #
    # 0 Match a set of characters:
    #
    # I RE1|RE2; Match either RE1 or
    # REZ non-greedy
    #
    # Match RE Inside parantheses and
    # indicate start and end of a group
    #
    # With RE is the resulting regular expre:
    #
    # jon.
    #
    # Special characters must be escaped with \ if
    # it should match the character literally
    #
    # Methods of ‘re’ module
    #
    # re.compile( Compile a regular
    # pattern, expression pattem into a
    # flags=0) regular expression object.
    # Can be used with match),
    # search() and others.
    # re.search( Search through string
    # pattern, matching the first location
    # string, of the RE. Returns a match
    # flags=0 object or None
    # re.match( _f zero or more characters
    # pattern, at the beginning of a string
    # string, match pattem return a
    # flags=0) match object or None
    # re.tullmatch( If the whole string matches
    # pattern, the pattern return a match
    # string, object or None
    # flags=0)
    # re.split( Split string by the occurr-
    # pattern, ences of pattern maxsplit
    # string, times if non-zero. Returns
    # maxsplit=0, alist of all groups.
    # flags=0)
    # reindal( Return all non-overlapping
    # pattern, matches of pattern in string
    # string, as list of strings.
    # flags=0)
    # re.finditer( Return an iterator yielding
    # pattern, match objects over all
    # string, non-overlapping matches
    # flags=0) for the pattern in string
    #
    # python regular expression (regex) Cheat Sheet
    # by mutanclan (mutanclan) via cheatography.com/79625/cs/19404/
    #
    # Methods of ‘re’ module (cont)
    #
    # resub( —_Retumm the string obtained by
    # pattern, _replacing the leftmost non-ov-
    # rep, erlapping occurrences of
    # string pattern in string by the repla-
    # count=0, cement repl. repi can bea
    # flags=0) function.
    #
    # resubn( Like sub but return a tuple
    # pattern, (new_string,
    #
    # repl, number_of_subs_made)
    # string,
    #
    # count=0,
    #
    # flags=0)
    #
    # reescape( Escape special characters in
    # pattern) —_ pattern
    #
    # re.purge() Clear the regular expression
    #
    # cache
    #
    # In raw string notation =" text" there is no
    # need to escape the backslash character
    # again.
    #
    # >>> re.match (e"\W(.)\1\W", * £€
    # ")
    #
    # <re.Match object; span=(0, 4),
    #
    # nate}
    #
    # ££ '>
    # >>> rematch (*\\W(.)\\1\\W",
    # ff *)
    #
    # <te.Match object; span=(0, 4),
    #
    # ff >
    #
    # hitps://docs.python.org/3/howta/regex.htm!
    #
    # https://docs.python.org//ibrary/re.htm!

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
