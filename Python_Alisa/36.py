#36.  Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#Пример:
#[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from random import *

nums = [randint(1, 9) for i in range(10)]
print('\nCписок: ', nums)

def create(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups

print('\nВозрастающая последовательность: ', create(nums))
