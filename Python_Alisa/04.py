#4.	Показать первую цифру дробной части числа 

#в строках:
# num = float(input('Введите число: '))
# num1 = str(float(num))
# num2 = num1.split(' ')
# print(num2)
# print(type(num3))
# num3 = num2[1]
# #print(num3)
# num_fin = num3[0]
# print((num_fin))

num = float(input('Введите число: '))
a = int((num*10) % 10)
print(a)