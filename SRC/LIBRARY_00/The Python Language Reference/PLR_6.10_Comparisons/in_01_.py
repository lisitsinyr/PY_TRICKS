#------------------------------------------
# in_01_ ():
#------------------------------------------
def in_01_ ():
    """in_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', in_01_.__name__)
    print ('#-----------------------------')

    # https://t.me/pyth0n_er/535
    # Находим подстроку
    #
    # Ключевое слово in используется для проверки, содержится ли
    # элемент в последовательности (список, кортеж, строка) или
    # словаре.
    # Возвращает логическое значение True если элемент находится в
    # последовательности/словаре, False если нет.
    #
    # Что нужно знать про поиск подстроки в строке:
    # — Поиск чувствителен к регистру символов, т. е. различает
    # заглавные и строчные буквы.
    # — Подстрока может состоять из одного символа.
    # — Поиск осуществляется слева направо по всей строке.
    # — Как только вхождение подстроки найдено — поиск
    # прекращается.
    # — Можно искать все вхождения подстроки, обернув проверку в
    # цикл.
    #
    # text = "Hello world"
    # substring = "or"
    #
    # print(substring in text) # True
    # # [IpoBepseM, eCTb NM NogscTpoka "or
    # # Bo3zBpawyaetca True, T.K. "
    #
    # u
    #
    # B cTpoke text
    # or” mpucyTcrByerT
    #
    # substring = "OL"
    #
    # print(substring in text) # False
    #
    # # IlpoBepsem Hafnuyue nogctpoKu “Ol”
    #
    # # Bo3Bpauaetca False, T.K. “OL" orcytcrByer B text
    #
    # text = "Hello WORLD"
    #
    # substring = "world"
    #
    # print(substring in text) # False
    #
    # # Tlonck 4yBCTBUTeNeH K perucTpy, no3TOMy “world” He HaiZe}
    # lmao


#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    in_01_ ()
#endif

#endmodule
