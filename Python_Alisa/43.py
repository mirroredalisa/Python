#43.  Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#Пример:
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


from random import *

nums = [randint(1, 10) for i in range(10)]
print('Задан список: ', nums, '\n')

nums = [i for i in nums if nums.count(i) == 1]            
#nums = list(filter(lambda x: nums.count(x) == 1, nums))   # другой способ

print('Список уникальных элементов: ', nums)








