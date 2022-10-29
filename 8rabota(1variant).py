#первая часть
from random import *
N=int(input("Введите объём матрицы(NxN):"))
a=[]
z=0
counter=0
for i in range (N):
    b=[]
    for j in range(N):
        b.append(randint(-10,10))
    a.append(b)
for i in range(N):
    for j in range(N):
        if i<j:
            if a[i][j]>0:
                z+=1
                counter += a[i][j]
print('Число положительных эллементов над главной диагональю: ', z, '\nСумма положительных эллементов над диагональю:',counter)
for i in range(N):
    for j in range(N):
        print(a[i][j],end="   ")
    print()



#вторая часть
from random import *
N=int(input('\nКоличество строк матрицы: '))
M=int(input('Количество столбцов матрицы: '))

A = []
for i in range(N):
    B=[]
    for j in range(M):
        B.append(randint(0,10))
    A.append(B)

print('Исходный массив:')
for i in range (N):
    for j in range(M):
        print(A[i][j], end='   ')
    print()

for i in range(N):
    a_min = 0
    b_min = A[i][0]
    for j in range(M):
        if A[i][j] < b_min:
            a_min = j
            b_min = A[i][j]
    zam2 = A[i][0]
    A[i][0] = A[i][a_min]
    A[i][a_min] = zam2

for i in range(N):
    a_max = 0
    b_max = A[i][0]
    for j in range(M):
        if A[i][j] > b_max:
            a_max = j
            b_max = A[i][j]
    zam2 = A[i][M-1]
    A[i][M-1] = A[i][a_max]
    A[i][a_max] = zam2

print('\nИзмененный массив:')
for i in range(N):
    for j in range(M):
        print(A[i][j], end='   ')
    print()