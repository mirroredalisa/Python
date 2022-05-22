#26.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

import random
def Get_random_int(): return random.randint(1,10)
n = Get_random_int()
print(f"Задано число: {n}") 


def fibonacci(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return fibonacci(index-1) + fibonacci(index-2)


list = [fibonacci(i) for i in range(1, n+1)]
#print(list)
list = list[::-1] + list[1:]
print(list, '\n')


