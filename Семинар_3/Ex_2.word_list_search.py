# # Задайте список, состоящий из произвольных слов,количество задает пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке, либо сообщит, что ее нет.

# in
# >> 6
# out 
# >> ['hfg','fgh','fgh','fhg','ffg','ffh']

# in
# >> ffg 

# out 
# >> 1

from random import choices
def list_new(n, word):
    new_list = []
    for i in range(n):
        a = choices(word, k=3)
        new_list.append(''.join(a))
    return new_list

def list_search(my_list, word_key):
    if my_list.count(word_key) > 1:
        n = my_list.index(word_key)
        print(my_list.index(word_key, n+1))
        print('Yes')
    else:
        print(-1)
res = list_new(20, 'abc')
print(res) 
list_search(res, input())       
