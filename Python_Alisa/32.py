#32.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import*

list = [randint(1, 10) for i in range(1, 10)]
list1 = []
print(list)
for i in list:
    if list.count(i) == 1:
        list1.append(i)
print(list1)



