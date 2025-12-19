#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/pythonl/4768
    # 🐍 Как просто создать мультисловарь (Multi-dictionary) в
    # Python
    #
    # Хочешь, чтобы один ключ в словаре указывал на несколько
    # значений?
    #
    # Легко!
    #
    # Используй collections.defaultdict и встроенный list:
    #
    #
    # from collections import defaultdict
    #
    # multidict = defaultdict(list)
    # multidict["SW"].append("Han Solo")
    # multidict["SW"].append("R2D2")
    #
    # 🔁 Теперь каждый ключ по умолчанию сопоставляется с пустым
    # списком. А append добавляет новое значение в этот список.
    #
    # Но будь внимателен: это немного “обман”. На самом деле
    # словарь всё ещё отображает один ключ → одно значение. Просто
    # это значение — список, в который ты уже сам кладёшь что
    # угодно.
    #
    # Почему defaultdict удобен?
    # Потому что тебе не нужно проверять, есть ли ключ в словаре.
    # Пустой список будет создан автоматически при первом
    # обращении к ключу.
    #
    #
    # Multi-dictionariy
    #
    # Mo>KHO CO3faTb CNOBaPb, CONOCTABNAIOLLINN ODHOMY
    # KMIOUY HECKONbKO 3HaYeHUN. Ilpoue BCero 3TO CHenaTb
    # c nomoulblo collections.defaultdict u BCTDOeHHOrO
    # Tuna List.
    #
    # 7 ‘ Mo YMOJI4YAaHUtO BCE
    # from collections import
    # KNIOUN COCOTaBNAIOTCCA
    #
    # defaultdlict ~. CMyCTbIM CnucKoM:
    #
    # multidict = defaultdict(list) »
    # print(multidict["Sw"])
    #
    # #[]
    # O6paulascb K Kmroyy U Lo print (multidict["Lotr’)
    # Ho6aBnaa SneMeHTHI, BbI a #[]
    #
    # ConocTaBnaeTe oHOMy =!
    # KmIO“Y HECKONbKO 3HaYeHUIN.
    #
    # multidict["SW'].append("Han Solo")
    # multidict["SW'].append ('R2D2') ¢-.
    # print(multidict['SW'] # ['Han Solo', \
    # R2 D2") \

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
