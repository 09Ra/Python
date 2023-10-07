# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# Решение 1 доработать
# number=int(input("Введите натуральное число больше 1 : "))
# quantity_fibonacci=int(input("Введите количество элементов строки Фибоначчи: "))
# element_value=0
# list_fibonacci=[0,1]
# i=1
# j=0
# while i>=1 and i<=quantity_fibonacci:
#     element_value=list_fibonacci[i-1]+list_fibonacci[i]
#     list_fibonacci.append(element_value)
#     i=i+1
# print(list_fibonacci)
# while j>0 and j<quantity_fibonacci:
#     if number!=list_fibonacci[j]:
#         j=j+1
#     elif number==list_fibonacci[j]:
#         print(i)
#     else:
#         print("-1")


number=input("Введите число: ")

while not number.isdigit():  # проверяем тип введенного number
    print("Вы ввели не целое число")
    number=input("Введите число: ")
    
number=int(number)

fib1=0 # Первый элемент строки Фибоначчи
fib2=1 # Второй элемент строки Фибоначчи
count=2 
while fib2<number:
    fib2,fib1=fib1+fib2,fib2 # Множественное присваивание
    count+=1
if fib2==number:
    print(count)
else:
    print(-1)    
