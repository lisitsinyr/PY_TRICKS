#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/PythonPortal/4379
    # Как заархивировать файлы в Python за 5 строк
    #
    # Стандартный модуль zipfile делает всё просто:
    #
    # import zipfile
    #
    # files = ['file1.txt', 'file2.txt']
    # with zipfile.ZipFile('pycl.zip', 'w') as zipf:
    #     for file in files:
    #         zipf.write(file)
    #
    # print("ZIP file created!")
    #
    # На выходе — pycl.zip с нужными файлами.
    #
    # Полезно для бэкенда, автосборки, логов 💪

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
