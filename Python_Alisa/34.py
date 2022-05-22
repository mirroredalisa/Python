#34.	Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

data = open('34-1.txt', 'r') 
stroka1 = str(data.readline())
stroka1 = stroka1.replace("=0","") # Убираем лишнее
stroka1 = stroka1.replace("= 0","") # Убираем лишнее
print(stroka1)
data.close

# Берём данные из 2 файла
data = open('34-2.txt', 'r')
stroka2 = str(data.readline())
print(stroka2)
data.close

# объединяем две строки и записываем результат в файл
s1_s2 = stroka1 + '+ ' + stroka2
print (s1_s2)

data = open('34-3.txt', 'w') 
data.write(s1_s2)
data.close

# СЧИТЫВАЕМ ИЗ ФАЙЛА В ПЕРЕМЕННУЮ И ПЕЧАТАЕМ ЕЁ:
with open('34-3.txt', 'r') as data:
    stroki = data.read() 
    print(type(stroki))
    print(stroki)



