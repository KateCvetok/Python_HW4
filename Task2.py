# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


with open('HomeWork4.txt', 'r', encoding='utf-8') as file:
    number = file.readline()
N = int(number)
new_list = []
i = 2
while i <= N:
    if N % i == 0:
        new_list.append(i)
        N //= i
    else:
        i += 1
print(new_list)
