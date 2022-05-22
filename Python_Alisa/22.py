#22.	Найти сумму чисел списка, стоящих на нечетной позиции.

import random
def Get_random_int(): return random.randint(5, 10)
n = Get_random_int()
#print(f"Длина списка: {n}")

from random import *
spisok = []
spisok = [randint(1, 9) for i in range(0,n)]
print(f"Список сгенерирован: {spisok}")
print('Сумма чисел списка, стоящих на нечетной позиции: ', sum(spisok[1::2]), '\n')


