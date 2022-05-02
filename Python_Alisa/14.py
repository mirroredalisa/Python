#14.	Подсчитать сумму цифр в вещественном числе.

import os
import random

a = random.uniform(1, 10)
print('Задано число:', a)

a = str(a).replace('.', '')    
print(a)
summa = sum(map(int, a))        
print('Сумма цифр данного числа равна:', summa, '\n')