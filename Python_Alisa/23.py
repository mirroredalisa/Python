#23.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

import random
def Get_random_int(): return random.randint(5, 10)
n = Get_random_int()
#print(f"Длина списка: {n}")

from random import *
spisok = []
spisok = [randint(1, 9) for i in range(0,n)]
print(f"Список сгенерирован: {spisok}")

spisok1 = []
for i in range ( 0, ((len(spisok) + 1)//2) ):
    spisok1.append(spisok[i] * spisok[-1-i]) 
print(f"Результат: \n{spisok1}")