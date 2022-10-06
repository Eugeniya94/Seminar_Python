# Напишите программу, которая будет принимать на вход дробь
#  и показывать первую цифру дробной части числа.

num = float(input())
new_num = int(num*10%10)
if new_num!=0:
    print(new_num)
else:
    print('no')    