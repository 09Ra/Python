# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# Решение №1
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# set_1 = set(list_1)  # преобразовываем список в множество
# print(list_1)
# print(set_1)
# print(len(set_1))

# Решение 2 

# import random # Импортируем модуль random

# random_list_1=[random.randint(1,10) for i in range(15)] # Создаем рандомный список из 15 элементов с значениями от 1 до 10
# print(random_list_1)
# set_1=set(random_list_1) # преобразовываем список в множество
# print(set_1)
# print(len(set_1))



#Решение №3 Кирилл Панфилов

from random import randint
 
print(list_1 := [randint(-5,5) for _ in range(1,10)]) 
print(len(set(list_1)))