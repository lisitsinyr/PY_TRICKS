#------------------------------------------
# _01_ ():
#------------------------------------------
def _01_ ():
    """_01_"""
#beginfunction
    print (f'#-----------------------------')
    print (f'# {_01_.__name__}')
    print (f'#-----------------------------')

    # https://t.me/pyth0n_er/1053
    # ➡️NamedTuple
    #
    # NamedTuple - это подтип кортежа, который позволяет объявлять собственные именованные типы, которые могут использоваться в качестве структуры данных. Он предоставляет возможность определить тип данных с помощью именованных полей. Каждое поле имеет свой собственный тип данных. Это может быть полезно в случаях, когда вам нужно создать объекты с определенными свойствами.
    #
    # К примеру, если вы создаете объекты, представляющие собой записи в базе данных, вы можете использовать NamedTuple, чтобы создать тип данных, содержащий поля, соответствующие полям в таблице.
    #
    # from collections import namedtuple
    #
    # Person = namedtuple('Person', ['name', 'age'])
    #
    # person1 = Person(name='John', age=30)
    # person2 = Person(name='Jane', age=25)
    #
    # print(person1.name)  # John
    # print(person2.age)  # 25
    #
    # Или например:
    #
    # from collections import namedtuple
    #
    # Person = namedtuple('Person', 'name age')
    #
    # person1 = Person('John', 30)
    # person2 = Person(name='Jane', age=25)
    #
    # print(person1.name)  # John
    # print(person2.age)  # 25

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    _01_ ()
#endif

#endmodule
