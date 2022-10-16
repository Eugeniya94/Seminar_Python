# Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import choices


def my_list(size):
    num_list = choices(range(1, size*2),k=size)
    return num_list
#print(my_list(int(input(':'))))    
end_list = my_list(int(input(':')))

def sets_num(my_list:list):
    new_list=[]
    for i in range(len(my_list)):
        p = my_list[i]
        n_list = [p]
        for j in range(i+1, len(my_list)):
            if my_list[j]>p:
                p=my_list[j]
                n_list.append(p)
        if len(n_list)>1:
            new_list.append(n_list) 
    return(new_list)

print(end_list, sets_num(end_list), sep='\n')

