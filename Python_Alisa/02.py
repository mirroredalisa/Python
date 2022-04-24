#2.	Найти максимальное из пяти чисел 


massive = [1, 13, 54, 8, 6]
#Другой способ:
#print (massive)
#print ('Максимальное число: ', max (massive))

max = massive[0]
for i in massive:
    if i>max:
        max = i
print ('Максимальное число: ', max, '\n')
