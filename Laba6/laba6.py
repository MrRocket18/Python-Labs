"""Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования 
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов 
(которое будет сокращать количество переборов) и целевую 
Вариант 21:
Составьте все различные правильные дроби из чисел 3, 5, 7, 11, 13, 17.
"""


import timeit
from itertools import combinations
# Часть 1
def algoritm(mas):
    fractions=[]
    for numerator in mas:
        for denominator in mas:
            if numerator < denominator:
                fractions.append((numerator,denominator))
    return fractions

def functionaly(mas):
    fractions=[]
    for numerator, denominator in combinations(mas,2):
        if numerator < denominator:
            fractions.append((numerator,denominator))
    return fractions
# Часть 2
def find_max_fraction_functionaly(numbers):
  max_fraction = (0, 1)
  max_value = 0
  fractions = [
    (numerator, denominator)
    for numerator, denominator in combinations(numbers, 2)
    if numerator < denominator and numerator + denominator < 40
  ]
  for fraction in fractions:
      value = fraction[0] / fraction[1]
      if value > max_value:
        max_value = value
        max_fraction = (fraction[0], fraction[1])
  return max_fraction

def find_max_fraction_algoritm(numbers):
  fractions=[]
  max_fraction = (0, 1)
  max_value = 0
  for numerator in numbers:
    if numerator<19:
      for denominator in numbers:
        if  numerator < denominator and numerator + denominator < 40:
          fractions.append((numerator,denominator))
  for fraction in fractions:
      value = fraction[0] / fraction[1]
      if value > max_value:
        max_value = value
        max_fraction = (fraction[0], fraction[1])
  return max_fraction

spis=[]
for i in range (3,200,2):
   spis.append(i)

# Часть 1
result_algoritm = algoritm(spis)
time_algoritm = timeit.timeit("algoritm(spis)",globals=globals(),number=1)
print(f"Результат: {result_algoritm}\nАлгоритмически время: {time_algoritm} сек.")

result_functionaly = functionaly(spis)
time_functionaly = timeit.timeit("functionaly(spis)",globals=globals(),number=1)
print(f"Результат: {result_functionaly}\nС помощью функции время: {time_functionaly} сек.")

# Часть 2
result_find_max_fraction_algoritm = find_max_fraction_algoritm(spis)
time_find_max_fraction_algoritm = timeit.timeit("find_max_fraction_algoritm(spis)",globals=globals(),number=1)
print(f"Результат: {result_find_max_fraction_algoritm}\nС помощью функции время: {time_find_max_fraction_algoritm} сек.")

result_find_max_fraction_functionaly = find_max_fraction_functionaly(spis)
time_find_max_fraction_functionaly = timeit.timeit("find_max_fraction_functionaly(spis)",globals=globals(),number=1)
print(f"Результат: {result_find_max_fraction_functionaly}\nС помощью функции время: {time_find_max_fraction_functionaly} сек.")