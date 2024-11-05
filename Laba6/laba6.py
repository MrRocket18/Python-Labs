"""Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования 
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов 
(которое будет сокращать количество переборов) и целевую 
Вариант 21:
Составьте все различные правильные дроби из чисел 3, 5, 7, 11, 13, 17.
"""


import time
from itertools import combinations
def algoritm(mas):
    fractions=[]
    for numerator in mas:
        for denominator in mas:
            if numerator < denominator:
                fractions.append((numerator,denominator))
    return fractions

def functionaly(mas):
    fractions=[]
    for pair in combinations(mas,2):
        numerator, denominator = pair
        if numerator < denominator:
            fractions.append((numerator,denominator))
    return fractions

def find_max_fraction(numbers):
  max_fraction = (0, 1)
  max_value = 0
  for pair in combinations(numbers, 2):
    numerator, denominator = pair
    if numerator < denominator and numerator + denominator < 20:
      value = numerator / denominator
      if value > max_value:
        max_value = value
        max_fraction = (numerator, denominator)
  return max_fraction

spis=[3, 5, 7, 11, 13, 17]

start_time = time.time()
result_algoritm = algoritm(spis)
end_time = time.time()
time_algoritm = end_time - start_time

start_time = time.time()
result_functionaly = functionaly(spis)
end_time = time.time()
time_functionaly = end_time - start_time

start_time = time.time()
result_find_max_fraction = find_max_fraction(spis)
end_time = time.time()
time_find_max_fraction = end_time - start_time

print(f"Результат: {result_algoritm}\nАлгоритмически время: {time_algoritm} сек.")
print(f"Результат: {result_functionaly}\nС помощью функции время: {time_functionaly} сек.")
print(f"Результат: {result_find_max_fraction}\nС помощью функции время: {time_find_max_fraction} сек.")