#1.	По двум заданным числам проверить является ли одно квадратом второго 

#Полезное на будущее:

# Для очистки предыдущих результатов на экране консоли:
#import os
#os.system("cls")

#Мапы:
#a, b = map(int, input().split())
#print(bool(a == b ** 2 or b == a ** 2))

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
if a == b**2 or b == a**2:
    print('Одно из чисел является квардратом другого')
else:
    print('Одно из чисел НЕ является квардратом другого')
