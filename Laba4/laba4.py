"""Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу. 
Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения. 
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Вариант 21:
Двоичные числа, не превышающие 102410 расположенные в порядке возрастания. Для каждой такой последовательности минимальное число вывести прописью.
"""
import re
def replace_non_binary(text):
  result = re.sub(r'\b(1[01]{10}|[01]{11,})\b|[^01\s]',",",text)
  result = result.split(",")
  while("" in result):
        result.remove("")
  return result
s=[]
f=open("test.txt","r")
while True:
    buf = f.readline()
    if not buf: break
    replaced_text = replace_non_binary(buf)
    for posledovatelnost in replaced_text:
        bin_number=posledovatelnost.split()
        for i in range (len(bin_number)-1):
                ch1=int(bin_number[i],2)
                ch2=int(bin_number[i+1],2)
                if ch1<ch2:
                    if len(s)==0:
                        s.append(bin_number[i])
                        propis=re.sub(r'1',"один ",bin_number[i])
                        propis=re.sub(r'0',"ноль ",propis)
                        print(propis)
                else:
                    s=[]
f.close()         