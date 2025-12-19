#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # Link: https://t.me/PythonPortal/4446
    #
    # Дата: 2025-06-01 06:07:00+00:00
    #
    # Title: Python Portal
    #
    # **Совет по Python:
    # **
    # Чтобы посчитать количество вхождений элементов, используйте
    # `Counter` из модуля `collections`
    #
    # Например у нас словарь, где ключ — это ID устройства, а
    # значение — его производитель.
    #
    # ```devices_vendors = {
    #     'device001': 'Cisco',
    #     'device002': 'Juniper',
    #     'device003': 'Cisco',
    #     'device004': 'Arista',
    #     'device005': 'Cisco'
    # }```
    #
    # > Выполняем подсчёт:
    #
    # ```vendor_counts = Counter(devices_vendors.values())```
    #
    # Здесь берутся все значения[ ](https://t.me/PythonPortal)из словаря (`.values()`), т.е. список вендоров:` ['Cisco', 'Juniper', 'Cisco', 'Arista', 'Cisco']`, и Counter считает, сколько раз каждый встретился.
    #
    # > Выводим и получаем:
    #
    # ```Counter({'Cisco': 3, 'Juniper': 1, 'Arista': 1})```
    #
    # from collections import Counter
    #
    # devices_vendors = {
    #
    # "deviceQ01': 'Cisco',
    # "deviceoo2': 'Juniper',
    # "device@03': 'Cisco',
    # "device004': 'Arista',
    # "deviced05': 'Cisco'
    #
    # vendor_counts = Counter(devices_vendors.values())
    #
    # print (vendor_counts)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
