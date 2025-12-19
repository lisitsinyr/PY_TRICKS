#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/PythonPortal/4258
    # Не используйте случайные строковые значения в Python
    #
    # Вместо этого используйте StrEnum из модуля enum.
    #
    # Это позволяет сгруппировать строковые значения и держать их
    # организованными.
    #
    # Кроме того, это помогает IDE корректно подсказывать
    # автодополнения при использовании этих значений.
    #
    # Идеально подходит, например, для перечисления возможных
    # аргументов функций ☕️
    #
    # NepeuncnenHua CTpOKOBbIX 3HaYeHUN
    #
    # Npu co3qanun pasnu4Hbix CTpOKOBbIX 3Ha4eHM — HanpuMep, ana onuni dyHKunn
    # Unu KOHurypauni — BbI Mo>KeTe CrpynnupoBaTb UX C NOMOLUbIO CTPOKOBOrO
    # nepeuucneHua StrEnum u3 Mogyna enum.
    #
    # = ‘ SiR a ‘
    # from enum import StrEnum. —|~~ def move(direction: Direction) -> None:
    #
    # ae = if direction == Direction.UP:
    # class Direction(StrEnum): print("Going up.")
    # UP = "UP" elif direction == Direction.DOWN:
    # DOWN = "DOWN" print("Going down.")
    # else:
    # ——— raise ValueError()
    # Ecnu HY)KHO, BbI MO)KETe
    # UCNOMb30BaTb CTPOKy
    # HanpsaMmyto BO Bpema
    # fHoarenien marr move(Direction.UP) # Going up.
    # Takasa CTpoK . a P '
    #
    # npoupét aseaaey Paro) >> move("DOWN") # Going down. (Doesn't type-check. )
    #
    # ! Python 3.11+ only. @PythonPortal

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
