''' Декларативное программирование:
Задача 4: Поиск уникальных элементов в списке.
Напишите программу, которая создает новый список, 
содержащий только уникальные элементы из исходного списка.
'''
old_list = [7, 7, 3, 3, 5, 5, 5, 9, 9, 3]
new_list = list(set(old_list))
print(new_list) 