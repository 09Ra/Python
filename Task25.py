# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов 
# добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


# Решение №1

# import random

# from random import choices, sample, randint  # hoices- заполняет рандомно повторяющимися буквами, sample- заполняет уникальными не повторяющимися буквами

# import string

# rnd=random.randint(5,50) # рандомно задаем количество элементов в строке

# stroka=(''.join(random.choices(string.ascii_letters, k=rnd)))
# stroka=str(stroka.upper())
# stroka=list(stroka)
# print(*stroka)
# s=set(stroka)


# for i in s:
#     count=0
#     for j in range(len(stroka)):
#         if stroka[j]==i and count>0:
#             stroka[j]=f'{stroka[j]}_{count}'
#             count+=1
#         if stroka[j]==i:
#             count+=1
# print(*stroka)     


# Решение №2
 
# list_1 = "a a a b c a a d c d d".split() 
# list_1.reverse()
# print(list_1)

# for i in range(len(list_1)):
#     list_1[i]=f"{list_1[i]}_{list_1.count(list_1[i])-1}"
# list_1.reverse()  #выводит элементы списка в обратном порядке
# list_1=" ".join(list_1) 

# print(list_1)

#Решение №3

list_1 = "a a a b c a a d c d d".split() 

dict_1={}
for el in list_1:
    if el in dict_1:
        dict_1[el]+=1
        print(f'{el}_{dict_1[el]}', end=" ")
    else:
        dict_1[el]=0
        print(el, end=" ")    
        
    
                      