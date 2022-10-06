# Напишите программу, которая принимает на вход число N  и выводит все числа от -N до N.

# num = int (input('Введите число: '))
# for i in range(-num,num+1):
#     if num < 0:
#         print()
# print(i, end=',')

num = int(input())
neg_num = -num
while num!=neg_num:
    print(neg_num, end=', ')
    if num > 0:
        neg_num +=1
    else:
        neg_num -=1
