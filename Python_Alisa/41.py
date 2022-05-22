#41.  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
#Пример:
#На сжатие:
#Входные данные:
#WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#Входные данные:
#12W1B12W3B24W1B14W

with open('41.txt', 'r') as data:
    string = data.readline()

count = 1
s = ""
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
    
        else:
            a = string[i]
            s+= str(count) + string[i]
            count = 1
s+= str(count) + string[i]
print(s)
with open('41-1.txt', 'w') as data:
    data.write(s)






