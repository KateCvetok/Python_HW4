# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
with open('HomeWork4.txt', 'r', encoding='utf-8') as file:
    number = file.readline()
from math import pi

d = int(number)

print(f'Число Пи с заданной точностью {d} равно {round(pi, d)}')