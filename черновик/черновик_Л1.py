# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))
# c = a + b
# print('{} + {} = {}'.format(a, b, c))

# a, b, c = 1, 2, 3
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))
# range(*(1,5,2))



# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#         print(line)

#text = 'съешь ещё этих мягких французских булок'
# # print(len(text)) 
# #print('ещё' in text) # True
#print(text.isdigit()) # False
# #print(text.islower()) # True
# #print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#   print(c)


#text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
#print(text[::6]) # сеикакл
#print(text[2:9] + text[-5] + text[:2]) # ...

numbers = list(range(1,6))
for i in numbers:
    i *= 2
    print(i)
print(numbers)


