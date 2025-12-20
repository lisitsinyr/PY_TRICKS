# -*- coding: UTF-8 -*-
__annotations__ = """
annotations:
************
Tricks_.py
"""
__doc__ = """
doc:
************
Tricks_.py
"""
"""
VENV:
    D:/PROJECTS_LYR/CHECK_LIST/DESKTOP/Python/VENV/P314/Lib/site-packages
"""
#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import sys
# appending a path
sys.path.append('D:/PROJECTS_LYR/CHECK_LIST/DESKTOP/Python/VENV/P314/Lib/site-packages')
from pathlib import Path

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# Tricks_ ():
#------------------------------------------
def Tricks_ ():
    """Tricks_"""
#beginfunction
    print ('#-----------------------------')
    print ('#', Tricks_.__name__)
    print ('#-----------------------------')

#endfunction

#------------------------------------------
# main ():
#------------------------------------------
def main ():
    """main"""
#beginfunction
    Tricks_ ()
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    print (__annotations__)
    print (__doc__)
    main()
#endif

#endmodule
