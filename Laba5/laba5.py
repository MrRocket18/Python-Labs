"""Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной форме. 
Обязательное требование – минимизация времени выполнения и объема памяти.
Вариант 21:
F(1) = 1, F(2) = 1, F(n) = (-1)**n*(F(n-2)+n/(2n)! + 2), при n > 2
"""


import math
import time

def recursive_f(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return (-1) ** n * (recursive_f(n - 2) + n / math.factorial(2 * n) + 2)

def iterative_f(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    f_prev = 1  # F(1)
    f_curr = 1  # F(2)
    factorial=24
    for i in range(3, n + 1):
      factorial=factorial*(i*2)*(i*2-1)
      f_next = (-1) ** i * (f_prev + i / factorial + 2)
      f_prev = f_curr
      f_curr = f_next
    return f_curr

for n in range(100,1000+1,25):

  start_time = time.time()
  result_recursive = recursive_f(n)
  end_time = time.time()
  time_recursive = end_time - start_time

  start_time = time.time()
  result_iterative = iterative_f(n)
  end_time = time.time()
  time_iterative = end_time - start_time

  print(f"F({n}) (рекурсивно): {result_recursive}, время: {time_recursive} сек.")
  print(f"F({n}) (итеративно): {result_iterative}, время: {time_iterative} сек.")
  print("="*100)
#Различия во времени начинают значительно увеличиваться при n=600