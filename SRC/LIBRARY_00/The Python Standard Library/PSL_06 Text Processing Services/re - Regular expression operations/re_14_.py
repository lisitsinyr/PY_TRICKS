#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/python_tg/1193
    # 🐍 Повторения и квантификаторы в регулярных выражениях
    #
    # Квантификаторы управляют количеством повторений символов:
    #
    # ⚪️a* — ноль или более вхождений;
    # ⚪️a+ — одно или более вхождений;
    # ⚪️a? — ноль или одно вхождение;
    # ⚪️a{n} — ровно n вхождений;
    # ⚪️a{n,} — n или более вхождений;
    # ⚪️a{n,m} — от n до m вхождений.
    #
    # 📌 Квантификаторы позволяют точно указать количество
    # повторений.
    # ‘HobyyeHne | “2
    #
    # NostTopeHna KM KBaHTNOnKaTOpbi
    # B peryJIAPHbIX BbIPaxKeCHNAX
    #
    # eee
    # import re
    # text = 'aaaa aa’
    #
    # # a* (Honb unn Gonee)
    # print(re.findall(r'a*', text)) # Beweget: ['aaaa', , aa", J
    #
    # # a+ (oguo wan 6onee)
    # print(re.findall(r'a+', text)) # Beiweget: ['aaaa', ‘aa’
    #
    # # a? (Honb uM ofHO)
    # print(re.findall(r'a?', text)) # Beweget: ['a', ‘'a', ‘a’, ‘a', '', ‘a', ‘a’, ' ']
    #
    # # a{n} (posHo n)
    # print(re.findall(r'a{4}', text)) # Boiweget: ['aaaa']
    #
    # # a{n,} (nN unw 6bonee)
    # print(re.findall(r'a{2,}', text)) # Beiseget: ['aaaa', ‘aa']
    #
    # # a{n,m} (oT nN go m)
    # print(re.findall(r'a{3,4}', text)) # Buiseget: ['aaaa']

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
