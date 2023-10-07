# Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)

from random import randint

line1=[randint(0,15) for i in range(randint(10,30))]
print(line1)

max_element=1 
n=0
while line1[n] !=0 and n < len(line1):
    if line1[n] > max_element:
        max_element=line1[n]
    else:    
        n+=1
        
print(f"Максимальный элемент последовательности равен {max_element}")    
    