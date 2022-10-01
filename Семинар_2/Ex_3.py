# from math import fabs
# from msilib.schema import tables


# Напишите программу, в которой пользователь будет задавать 2 строки, программа-определять
# количество вхождений одной строки в другую

# in-> gipopotampo
# >>po
# out >> 3

# in-> gipopotamo
# >> ta
# out>>1

# in-> gipopotamo
# >>fa
# out>> 0

string1 = input()
string2 = input()
print(string1.count(string2))
