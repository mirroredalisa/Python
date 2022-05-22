#24.	В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19



import random
def Get_random_int(): return random.randint(5, 10)
n = Get_random_int()
#print(f"Длина списка: {n}")

from random import *
spisok = []
spisok = [uniform(-10, 10) for i in range(0,n)] #вещественные числа
print(f"Список сгенерирован: {spisok}")

#отделяем целую часть от дробной
spisok2 = [] 
for i in spisok:
    if (abs(i) % 1) != 0: spisok2.append(abs(i) % 1)

#print(f"Дробные части: \n{spisok2}")
print('Максимальное значение дробной части: ', max(spisok2))
print('Минимальное значение дробной части:  ', min(spisok2))
print('Разница:            ', max(spisok2) - min(spisok2))