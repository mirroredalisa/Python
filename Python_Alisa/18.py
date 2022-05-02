#18.	Реализовать алгоритм перемешивания списка. 

import os
import random


list = [random.randint(1, 101) for item in range(10)]
print(list)
random.shuffle(list)
print(list, '\n')