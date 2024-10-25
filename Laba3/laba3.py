"""Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом), распознает, преобразует и 
выводит на экран объекты по определенному правилу. Объекты разделены пробелами. Преобразование делать по возможности через словарь. 
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.
Вариант 21.
Двоичные числа, не превышающие 1024 в десятичной расположенные в порядке возрастания. Для каждой такой последовательности минимальное число вывести прописью.
 """
def check2(chislo):
    for i in chislo:
        if i !="0" and i!="1":
            return False
    return True
def print_chislo(chislo):
    print("Минимальное число в последовательности:")
    for i in chislo:
        print(i, end=' ')
    print()
check=1024
s=[]
f=open("test.txt","r")
while True:
    buf = f.readline().split()
    if not buf: break
    for i in range(len(buf)-1):
        if check2(buf[i]) and check2(buf[i+1]):
            ch1=int(buf[i],2)
            ch2=int(buf[i+1],2)
            if ch1<check and ch2<check:
                if ch1<ch2:
                    if len(s)==0:
                        s.append(buf[i])
                        print_chislo(buf[i])
                else:
                    s=[]
            else:
                s=[]
        else:
            s=[]
f.close()