import random

length = int(input("Введите длинну пароля: "))
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUYWXYZ"
c = "0123456789"
d = "[]{}()*'/,_-!?"
all = a + b + c + d

password = "".join(random.sample(all,length))
print(password)
