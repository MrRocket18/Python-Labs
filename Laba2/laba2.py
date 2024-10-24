import random
import numpy as np
import matplotlib.pyplot as plt

def print_mat(n,mat_name):
    print("Матрица "+mat_name)
    for i in n:
        for j in i:
            print(j, end=' ')
        print()

n=int(input("Введите количество строк(столбцов) квадратной матрицы в интервале от 2 до 100.\nВаш выбор:"))

while n<2 or n>100:
    n=int(input("Вы ввели неверное число.\nВведите количество строк(столбцов) квадратной матрицы в интервале от 2 до 100.\nВаш выбор:"))

mid=n//2 + n%2 #центр матрицы 

if n%2!=0: #изменения у нечетной матрицы
     mid-=1


K=int(input("Введите число K.\nВаш выбор:"))

A=np.zeros((n,n))

metod=int(input("Введите число(метод), который хотите использовать:\n1-рандомный\n2-файловый\n3-генератор\nВаш выбор:"))
while metod < 1 or metod >3:
    metod=int(input("Вы ввели неверное число\nВведите число(метод), который хотите использовать:1-рандомный, 2-файловый, 3-генератор"))

if metod==1:
    A  = np.random.randint(-10,10, size=(n,n))

elif metod==2:
    file=open("matr2.txt","r")
    for i in range(n):
        stroka=file.readline().split()
        for j in range(n):
            A[i][j]=int(stroka[j])

else:
    for i in range(n):
        for j in range(n):
            if i<mid and j<mid:
                A[i][j]=1
            elif i>=mid and j<mid:
                A[i][j]=2
            elif i<mid and j>=mid:
                A[i][j]=3
            elif i>=mid and j>=mid:
                A[i][j]=4
            if n%2!=0 and (i==mid or j==mid):
                A[i][j]=0

print_mat(A,"A")

F=np.copy(A)

print_mat(F,"F")

plt.figure(figsize=(12, 9))
plt.axis([-10,10,0,n*n])
plt.title('Counting numbers in a matrix F',color='blue',fontsize=20, fontname='Times New Roman')
plt.xlabel('Number',color='blue',fontsize=20, fontname='Times New Roman')
plt.ylabel('Quantity',color='blue',fontsize=20, fontname='Times New Roman')
count_number=0
x=[]
y=[]
for i in range(2,n*n,2):
    y.append(i)
for k in range(-10,11):
    for i in range (n):
        for j in range (n):
            if F[i][j]==k:
                count_number+=1
                x.append(k)
    plt.plot([k],[count_number],'ro')
    count_number=0
plt.xticks(x, x)
plt.yticks(y, y)
plt.grid(True)


count_positive_in_F,count_negative_in_F,count_zero_in_F,count_even_numbers_in_F,count_odd_numbers_in_F=0,0,0,0,0

for i in range(n):
    for j in range(n):
        if F[i][j]>0:
            count_positive_in_F+=1
        elif F[i][j]<0:
            count_negative_in_F+=1
        else:
            count_zero_in_F+=1
        if F[i][j]%2==0:
            count_even_numbers_in_F+=1
        else:
            count_odd_numbers_in_F+=1

print(count_even_numbers_in_F,count_odd_numbers_in_F)

plt.figure(figsize=(10, 8))
type_of_numbers = ["Zero", "Positive", "Negative"]
counts_type_of_numbers = [count_zero_in_F,count_positive_in_F,count_negative_in_F]
plt.bar(type_of_numbers, counts_type_of_numbers)
plt.grid(axis='y')
plt.title("Type of numbers!",color='blue',fontsize=20, fontname='Times New Roman')
plt.xlabel("Type",color='blue',fontsize=20, fontname='Times New Roman')
plt.ylabel("Count",color='blue',fontsize=20, fontname='Times New Roman')


plt.figure(figsize=(10, 8))
x=[1,2]
plt.axis([0.5,2.5,0,n*n])
type_of_numbers_odd_and_even = ["Odd","Even" ]
counts_of_even_and_odd_numbers = [count_odd_numbers_in_F,count_even_numbers_in_F ]
plt.stem(x,counts_of_even_and_odd_numbers)
plt.xticks(x,type_of_numbers_odd_and_even)
plt.grid(axis='y')
plt.title("Type of numbers!",color='blue',fontsize=20, fontname='Times New Roman')
plt.xlabel("Type",color='blue',fontsize=20, fontname='Times New Roman')
plt.ylabel("Count",color='blue',fontsize=20, fontname='Times New Roman')
plt.show()

count_0_in_odd_columns_in_B=0

for i in range(mid):
    for j in range(0,mid,2):
        if F[i][j]==0:
            count_0_in_odd_columns_in_B+=1
print("Количество 0 в нечетных столбцах подматрицы B = ",count_0_in_odd_columns_in_B)

sum_in_even_lines_in_B=0

for i in range(1,mid,2):
    for j in range(mid):
        sum_in_even_lines_in_B+=F[i][j]
print("Сумма в четных строках подматрицы B = ", sum_in_even_lines_in_B)

if count_0_in_odd_columns_in_B > sum_in_even_lines_in_B:
   for i in range(mid):
        for j in range(mid):
            F[n-i-1][j],F[i][j]=F[i][j],F[n-i-1][j]

else:
    for i in range(mid):
        for j in range(mid):
            F[mid-1-i][n-1-j],F[i][j]=F[i][j],F[mid-1-i][n-1-j]

print_mat(F,"F изменённая")

det = int(np.linalg.det(A))
print("Оперделитель матрицы A =",det)

sum_diagonals_F = 0 
for i in range (n):
    sum_diagonals_F += F[i][i] + F[i][n-1-i]
    #print(F[i][i],",",F[i][n-1-i])

if n%2!=0:
    sum_diagonals_F-=F[mid][mid]

print("Сумма диагоналей матрицы F = ", sum_diagonals_F)

if ((det > sum_diagonals_F) & (det!=0)):
    A_minus_degree = np.linalg.inv(A)
    print_mat(A_minus_degree,"A**-1")

    A_T=np.transpose(A)
    print_mat(A_T,"A**T")

    A_minus_degree_multiply_by_A_T = np.dot(A_minus_degree,A_T)
    print_mat( A_minus_degree_multiply_by_A_T,"A**-1 * A**T")

    F_t = np.transpose(F)
    print_mat(F_t,"F**T")

    K_multiply_by_F_T=np.dot(K,F_t)
    print_mat(K_multiply_by_F_T,"K * F**T")

    result=np.subtract(A_minus_degree_multiply_by_A_T,K_multiply_by_F_T)
    print_mat(result,"Результат вычисления A**-1 * A**T - K * F**T ")
elif ((int(np.linalg.det(F))!=0)) & ((det < sum_diagonals_F)):
    A_T=np.transpose(A)
    print_mat(A_T,"A**T")

    F_minus_degree = np.linalg.inv(F)
    print_mat(F_minus_degree,"F**-1")

    G=np.triu(A)
    print_mat(G,"G")
    
    A_T_add_G=np.add(A_T,G)
    print_mat(A_T_add_G,"A**T + G")

    A_T_add_G_minus_F_minus_degree=np.subtract(A_T_add_G,F_minus_degree)
    print_mat(A_T_add_G_minus_F_minus_degree,"A**T + G - F**-1")

    result=np.dot(A_T_add_G_minus_F_minus_degree,K)
    print_mat(result,"Результат вычисления (A**T + G - F**-1)*K  ")

else: 
    print("Невозможно произвести вычисления т.к определитель равен 0")

