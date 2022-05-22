#37. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащий максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7] Порядок элементов менять нельзя

from random import *

nums = [randint(1, 9) for i in range(10)]
print('\nИсходный список: ', nums)

def create(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups

#все последлвательности
largest = 0
index = 0
massiv_spiskov = [] 
max_dlinna_spiska = 1
for i in range(len(nums)):
    i_spisok = create(nums[i:])
    if len(i_spisok) > max_dlinna_spiska : 
        max_dlinna_spiska = len(i_spisok) 
    #печать всех списков
    #print(i_spisok) 
    massiv_spiskov.append(i_spisok) 

print('\nСписок/списки, описывающие возрастающую последовательность, с максимальным количеством элементов: ')
for i in range(len(massiv_spiskov)):
    if max_dlinna_spiska == len(massiv_spiskov[i]): 
        print(massiv_spiskov[i])