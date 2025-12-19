#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')
https://t.me/c/1741591446/2349
Автоматизация сжатия файлов с помощью Python

import gzip
import shutil

def compress_file(input_file, output_file):
  with open(input_file, 'rb') as f_in:
    with gzip.open(output_file, 'wb') as f_out:
      shutil.copyfileobj(f_in, f_out)

input_file = 'test.txt'
output_file = 'test.rar'
compress_file(input_file, output_file)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
