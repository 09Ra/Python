# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

n=randint(10,50)
m=randint(10,50)
set1=set(randint(0,100) for i in range(n))
set2=set(randint(0,100) for i in range(n))
print(set1)
print(set2)
new_set=set1.intersection(set2)
print(sorted(new_set))