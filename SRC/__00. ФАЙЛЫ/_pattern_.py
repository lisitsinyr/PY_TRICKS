# -*- coding: UTF-8 -*-
__annotations__ = """
annotations:
************
_Pattern_.py
"""
__doc__ = """
doc:
************
_Pattern_.py
"""
"""
LIB:
    D:/PROJECTS_LYR/CHECK_LIST/DESKTOP/Python/VENV/P314/Lib/site-packages
"""
LIB = r'D:\PROJECTS_LYR\CHECK_LIST\DESKTOP\Python\VENV\P314\Lib\site-packages'

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import sys

# appending a path
sys.path.append(LIB)
from pathlib import Path

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# _Pattern_ ():
#------------------------------------------
def _Pattern_ ():
    """_pattern_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_Pattern_.__name__}')
    print (f'#-----------------------------')

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    print (__annotations__)
    print (__doc__)
    _Pattern_ ()
#endif

#endmodule
