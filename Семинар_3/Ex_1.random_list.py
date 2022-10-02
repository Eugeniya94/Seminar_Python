
# Задайте список, состоящий из произвольных чисел,количество задает пользователь.
# Напишите программу, определяющую, присутствует ли в заданном списке число,полученное от пользователя.

# in
# >>10
# >>13

# out 
# >> [13,11,21,7,14,5,1,16,14,15]
# >> Число 13 присутствует в списке

from random import sample
def num_in_list(count, number):
    if count<0:
        return"Error"
    my_list = sample(range(1, count*2),count)
    print(my_list)
    if number in my_list:
        return 'Yes'
    return 'No'

print(num_in_list(int(input()), int(input())))