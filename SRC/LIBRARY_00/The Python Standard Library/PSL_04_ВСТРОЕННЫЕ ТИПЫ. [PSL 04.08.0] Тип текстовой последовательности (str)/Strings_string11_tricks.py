from pathlib import Path

#------------------------------------------
# Strings_string11_tricks ():
#------------------------------------------
def Strings_string11_tricks ():
    """Strings_string11_tricks"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Strings_string11_tricks.__name__}')
    print (f'#-----------------------------')

    data = ('test', 'test1')
    a = (x for x in data)
    print(type (a))
    b = [x for x in data]
    print(type (b))

    data = Path ("Strings_.txt").read_text ().split ()
    a = (x.lower () for x in data)
    print(a)
    b = [x.lower () for x in data]
    print(b)
    data.clear ()

    data = Path ("Strings_.txt").read_text ().split ()
    a = all (x.lower () for x in data)
    print(a)
    b = all ([x.lower () for x in data])
    print(b)
    data.clear ()

    #--------------------------------------------------------
    # Как подставить переменную в строку
    #--------------------------------------------------------
    # В Python есть шесть способов подставить переменную в строку.
    # Не все из них социально приемлемые.
    # Если коротко, то преподаватель точно не завернёт работу, использующую .format:
    person1 = 'Александра'
    person2 = 'Александр'
    message_template = """Здравствуйте, {recipient}! На связи {sender}.
    ...
    С уважением,
    {sender}
    """
    message = message_template.format(recipient=person1, sender=person2)
    print(message)

    #------------------------------------------------------------
    # Как не надо
    # .format cо строковыми литералами
    # Выносить в параметры .format нужно только изменяющиеся данные. Не стоит писать
    #------------------------------------------------------------
    message_template = "{greeting}{comma} {recipient}{exclamation_point}"
    message = message_template.format(
        greeting='Здравствуйте', comma=',', recipient='Александра', exclamation_point='!'
     )
    print(message)
    # Параметры comma и exclamation_point всегда будут равны запятой и восклицательному знаку. Их надо делать частью шаблона:
    message_template = "{greeting}, {recipient}!"
    message = message_template.format(
        greeting='Здравствуйте', recipient='Александра',
     )
    print(message)
    # Если заранее известно, что и приветствовать мы всегда будем словом “Здравствуйте”, оно тоже станет частью шаблона:
    message_template = "Здравствуйте, {recipient}!"
    message = message_template.format(recipient='Александра')
    print(message)

    #------------------------------------------------------------
    # Сложение
    # Как было упомянуто в статье про арифметические операции над строками, их лучше избегать:
    #------------------------------------------------------------
    person1 = 'Александра'
    person2 = 'Александр'
    message = """Здравствуйте, """ + person1 + """! На связи """ + person2 + """.
    ...
    С уважением,
    """ + person2
    print(message)
    # Такие строки трудно читать и изменять.
    # replace
    person1 = 'Александра'
    person2 = 'Александр'

    message_template = """Здравствуйте, {recipient}! На связи {sender}.
    ...
    С уважением,
    {sender}
     """
    message = message_template.replace('{recipient}', person1)
    message = message.replace('{sender}', person2)
    print(message)
    # В сущности аналогичен .format, но менять количество и название переменных уже труднее. А ещё .format умеет, например, выравнивать строки, а replace так не может.
    #------------------------------------------------------------
    # Как ещё можно
    # В моменты, когда нужно форматирование строки в стиле printf
    # (функции из популярного системного языка C), используют оператор %.
    #------------------------------------------------------------
    # Начиная с версии 3.6 в Python появились f-строки — более удобная замена .format.
    #------------------------------------------------------------
    # С особо редких случаях прибегают к Template Strings.
    # ------------------------------------------------------------
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Strings_string11_tricks ()
#endif

#endmodule
