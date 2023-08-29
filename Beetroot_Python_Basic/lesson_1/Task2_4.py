from random import randint
list_1=[randint(1,10) for i in range(10)]
list_2=[randint(1,10) for i in range(10)]
list_3=list_1 + list_2
print(list_1)
print(list_2)
print(set(list_3))