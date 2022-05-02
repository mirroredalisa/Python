#16.	Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму

n = int(input('Введите число n: '))

massive = []

for i in range(1, n+1):
    massive.append(1+(1/i)**i)
print(f'{sum(massive):.2f}')