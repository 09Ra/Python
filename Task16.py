# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

import random

list_1=[random.randint(1,10) for i in range(20)]
print(list_1)

k=int(input("Введите число k: "))
coin=0
for i in range(len(list_1)):
    if list_1[i]==k:
        coin+=1
print("Число",k,"встречается в массиве", coin, "раз")    



   