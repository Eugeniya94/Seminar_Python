# Найдите корни квадратного уравнения Ax(2)+Bx+C = 0, с помощью модуля.
# Запросите значения A,B,C 3 раза. Уравнения и корни запишите в файл
from math import sqrt
def sqrt_r(a, b, c):
    d = b**2 - 4*a*c
    with open('sqrt.txt', 'a', encoding='utf-8') as my_f:
        my_f.write(f'{a}x(2) + {b}x + {c} = 0\n')
        if d>0:
            my_f.write(f'{(-b+sqrt(d))/(2*a)}\n')
            my_f.write(f'{(-b-sqrt(d))/(2*a)}\n')
        elif d==0:
            my_f.write(f'{-b/(2*a)}\n') 
        else:
            my_f.write('Нет корней') 
for i in range(3):
    sqrt_r(int(input('A: ')), int(input('B: ')), int(input('C: ')))         
              