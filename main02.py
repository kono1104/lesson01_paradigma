''' Императивное программирование: Задача 2:
 Поиск наименьшего числа в списке.
 Напишите программу, которая находит наименьшее 
 число в заданном списке с помощью цикла.
'''
numbers = [21, 12, 13, 3, 4, 7]
min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num

print(min_num)