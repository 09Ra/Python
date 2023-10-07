# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.


# Решение №1 Моя домашка
# import random

# list_1=[random.randint(1,10) for i in range(5)]
# print(list_1)
# list_2=[]

# k=int(input("Введите число k: "))

# min=1000
# coin=0
# for i in range(len(list_1)):
#     list_2.append(abs(list_1[i]-k))
#     for j in range(len(list_2)):
#        if list_2[j]<min:
#             min=list_2[j]
#             coin=j
# print(list_1[coin])    


# Решение №2 Эталонное решение

import random


list_1=[random.randint(1,10) for i in range(5)]
print(list_1)

k=int(input("Введите число k: "))

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)

               
       
            
      
            
