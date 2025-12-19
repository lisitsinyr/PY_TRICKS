#------------------------------------------
# Lists_list01_Expand ():
#------------------------------------------
def Lists_list01_Expand ():
    """Lists_list01_Expand"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {Lists_list01_Expand.__name__}')
    print (f'#-----------------------------')

    # 1. Использование метода append()
    my_list = [1, 2, 3, 4, 5]
    reversed_list = []
    for i in range(len(my_list) -1, -1, -1):
        reversed_list.append(my_list[i])
    print(reversed_list)

    # 2. Использование цикла
    my_list = [1, 2, 3, 4, 5]
    for i in range(len(my_list)//2):
        my_list[i], my_list[-i-1] = my_list[-i-1], my_list[i]
    print(my_list)

    # 3. Использование reversed()
    my_list = [1, 2, 3, 4, 5]
    reversed_list = list(reversed(my_list))
    print(reversed_list)

    # 4. Обращение с помощью срезов
    my_list = [1, 2, 3, 4, 5]
    reversed_list = my_list[::-1]
    print(reversed_list)

    # 5. Использование метода reverse()
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()
    print(my_list)
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Lists_list01_Expand ()
#endif

#endmodule
