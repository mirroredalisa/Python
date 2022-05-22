#29.	Найти НОК двух чисел

from random import *

a = randint(1, 100)
b = randint(1, 100)
print('a = ', a)
print('b = ', b)

for i in range(a*b, 1, -1):
    if i % a == 0 and i % b == 0:
        nok = i

print('НОК = ', nok, '\n')



