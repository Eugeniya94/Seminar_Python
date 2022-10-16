# ; Создайте список из N натуральных чисел.
# ; Среди чисел не хватает одного, чтобы выполнилось условие
# ; A[i]-1 = a[i-1].Найдите это число.

from random import choice

def fill_list(count: int):
    my_list = [x for x in range(count+1)]
    my_list.remove(choice(my_list))
    return my_list
#print(fill_list(int(input('Введите число: '))))  
new_list = fill_list(int(input('Введите число: ')))

def find(my_list: list):
    for i in range(1, len(my_list)):
        if my_list[i]-1 != my_list[i-1]:
            return my_list[i]-1
    return -1        
print(new_list, find(new_list))            

