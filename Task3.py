# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

with open('HomeWork4-2.txt', 'r', encoding='utf-8') as file:
    line = file.readline().split()
new_list = []
for i in line:
    if line.count(i) == 1:
        new_list.append(i)
print(new_list)
