"""С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N) заполняется случайным образом целыми числами в интервале [-10,10]. 
Для тестирования использовать не случайное заполнение, а целенаправленное, введенное из файла. 
Условно матрица имеет вид:
     2
 1       3
     4
21.	Формируется матрица F следующим образом: Скопировать в нее матрицу А и если сумма 
чисел, по периметру области 3 больше, чем произведение чисел по периметру области 2, 
то поменять симметрично области 2 и 3 местами, иначе 1 и 2 поменять местами
 несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: 
  A*F+ K*F T . Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import random

def print_mat(n,mat_name):
    print("Матрица "+mat_name)
    for i in n:
        for j in i:
            print(j, end=' ')
        print()
s2=1
s3=0
v1=[]
v2=[]
A,F,A_F,F_t,K_F_t,result=[],[],[],[],[],[]

n=int(input("Введите количество строк(столбцов) квадратной матрицы в интервале от 3 до 100.\nВаш выбор:"))

while n<3 or n>100:
    n=int(input("Вы ввели неверное число.\nВведите количество строк(столбцов) квадратной матрицы в интервале от 3 до 100.\nВаш выбор:"))

K=int(input("Введите число K.\nВаш выбор:"))

for i in range(n):
    A.append([0]*n)
    F.append([0]*n)
    F_t.append([0]*n)
    A_F.append([0]*n)
    K_F_t.append([0]*n)
    result.append([0]*n)

metod=int(input("Введите число(метод), который хотите использовать:\n1-рандомный\n2-файловый\nВаш выбор:"))
while metod < 1 or metod >2:
    metod=int(input("Вы ввели неверное число\nВведите число(метод), который хотите использовать:1-рандомный, 2-файловый"))

if metod==1:
    A = [[random.randint(-10,10) for i in range(n) ] for j in range(n)]
else:
    file=open("matr.txt","r")
    for i in range(n):
        stroka=file.readline().split()
        for j in range(n):
            A[i][j]=int(stroka[j])

print_mat(A,"A")

for i in range(n): #Копирование Матрицы А в матрицу F
    for j in range(n):
        F[i][j]=A[i][j]

for i in range(n): #считаем произведение элементов в области 2
    for j in range(n):
        if n>6:
                if (i < j) & (i < n - j - 1) & ((abs(i-j)==1) or i+j==(n-2)):
                        s2=s2*A[i][j]
                elif (i < j) & (i < n - j - 1) & (j>1) & (j<(n-2)) & (i==0):
                        s2=s2*A[i][j]
        elif (i < j) & (i < n - j - 1):
            s2=s2*A[i][j]
            
print("Произведение чисел во 2 области =",s2) 
for i in range(n): # считаем сумму элементов в области 3
    for j in range(n):
        if n>6:
            if (i < j)&(i > n - j - 1)&((abs(i-j)==1) or i+j==(n)):
                s3=s3+A[i][j]
            elif (i < j) & (i > n - j - 1) & (i>1) & (i<(n-2)) & (j==n-1):
                s3=s3+A[i][j]
        elif (i < j) & (i > n - j - 1):
                s3=s3+A[i][j]
print("Сумма в 3 области = ",s3)

if s3>s2:  # изменяем матрицу F 
    for i in range(n):
        for j in range(n):
            if (i < j) & (i < n - j - 1):
                F[i][j],F[n-j-1][n-i-1]=F[n-j-1][n-i-1],F[i][j]
                                                                
else:
    for i in range(n):
        for j in range(n):
            if (i>j) & (i < n - j - 1):
                F[i][j],F[j][n-i-1]=F[j][n-i-1],F[i][j]
      
print_mat(F,"F")

for i in range(n): #операция трансформации матрицы
    for j in range(n):
        F_t[j][i]=F[i][j]
print_mat(F_t,"FT")

 #операция умножения матрицы А на число K
for i in range(n):
    for j in range(n):
        K_F_t[i][j]=K*F_t[i][j]
print_mat(K_F_t,"K*FT")

 #операция умножения матриц А на F
for i in range(n): 
        for j in range(n):
            for k in range(n):
                A_F[i][j] += A[i][k]*F[k][j]
print_mat(A_F,"A*F")

 # операция суммы матриц 
for i in range(n):
    for j in range(n):
        result[i][j]=A_F[i][j]+K_F_t[i][j]
print_mat(result,"A*F+K*FT")
