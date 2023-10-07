# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Решение №1 с помощью срезов

# list_1=[1, 2, 3, 4, 5]
# k=int(input("Введите число k: "))
# list_2=[list_1[k-1:]+list_1[:k-1]] #  Используем срезы и сложение списков. -1 ставим, так как индексация списков начинается с 0
# print(*list_2)

# Решение №2 с помощью циклов

# list_1=[1, 2, 3, 4, 5]
# k=int(input("Введите число k: "))
# for i in range(len(list_1)-k):  
#     for j in range(len(list_1)-1):
#         list_1[j],list_1[j-1]=list_1[j-1],list_1[j]
# print(list_1)

# Решение №3 с помощью  функции insert

# from random import randint
 
# print(list_1 := [randint(-5,5) for _ in range(10)]) 

# k=int(input("Введите число k: "))

# for i in range(k):  
#     list_1.insert(0,list_1.pop(-1)) # Вставляем в индекс 0 последнюю позицию, которую и удаляем, т.к фунцкия pop возвращает элемент, который удаляет
# print(list_1)


# Решение №4 от Кирилла Панфилова

# from random import randint
 
# print(list_1 := [randint(-5,5) for _ in range(10)]) 

# k=int(input("Введите сдвиг: "))

# print(list_1[-k:]+list_1[:-k])


# Решение №5 от Кирилла Панфилова

from random import randint
 
print(list_1 := [randint(-5,5) for _ in range(10)]) 

k=int(input("Введите сдвиг: "))

new_list=[]

for i in range(len(list_1)):
    new_list.append(list_1[(i-k)%len(list_1)])
print(new_list)
