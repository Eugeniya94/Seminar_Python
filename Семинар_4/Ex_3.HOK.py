# Задайте 2 числа. Напишите программу, которая будет находить НОК(наименьшее общее кратное) этих 2 чисел.
from math import gcd
a = int(input(':'))
b = int(input(':'))
print(a*b//gcd(a,b))
print(gcd(a,b))