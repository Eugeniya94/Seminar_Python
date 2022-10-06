# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.


max = 0
for i in range(5):
    num = int(input())
    if num > max:
        max = num
print(num) 
       
