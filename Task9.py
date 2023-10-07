# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Решение 1
# number=int(input("Введите число: "))
# factorial=1
# i=0
# if number>0:
#     while i>=0 and i<number:
#         factorial=factorial*(number-i)
#         i+=1
#     print(number,"! равен", factorial)

# else:
#     print("0! равен 1")
    
    
# Решение 2
# number=int(input("Введите число: "))
# factorial=1
# while number>1:
#     factorial*=number
#     number-=1
# print("! равен", factorial) 


# Решение 3
number=input("Введите число: ")

while not number.isdigit():  # проверяем тип введенного number
    print("Вы ввели не целое число")
    number=input("Введите число: ")
    
number=int(number)

factorial=1

if number>0:
    while number>1:
        factorial=factorial*number
        number=number-1
    print(number,"! равен", factorial)    
else:
    print("0! равен 1")    
    
    

    
