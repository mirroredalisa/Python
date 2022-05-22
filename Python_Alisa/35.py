#35.  В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('35.txt', 'r') as data:
    stroka = data.read() 
    print(type(stroka))
    print('Все числа: ', stroka)

# перевод строки в массив 
spisok = stroka.split(' ')
print(type(spisok))
#print("Массив: ", spisok)

for i in range(1, len(spisok)):
    if (int(spisok[i]) - 1) != (int(spisok[i - 1])):
        print('Не хватает числа:', int(spisok[i]) - 1)

