#33.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from itertools import *
from random import randint

k = randint(2, 7)  # случайным образом выбираем степень
print('k = ', k)


def get_ratios(k):  # заполняем массив ratios случайными числами, первый элемент не нулевой
    ratios = [randint(1, 9) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 9)
    return ratios


def get_polynomial(k, ratios):  # вычисляем полином, передаем степень и массив коэффициентов
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in zip_longest(
        ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

data = open('33.txt', 'w') 
data.write(polynom1)
data.close