# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

a=int(input("Введите a: "))
b=int(input("Введите b: "))
c=int(input("Введите c: "))
if c % a == 0 or c % b == 0:
    print("yes")
else:
    print("no")    