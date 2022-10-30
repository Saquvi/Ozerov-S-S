#первая часть
n=int(input('Введите размер матрицы(NxN):'))
A=[]
sumn=0
for i in range (n):
    B=[]
    for j in range(n):
        B.append(int(input('Введите эллемент матрицы:')))
    A.append(B)

sum_count=0
for i in range (len(A)):
    counter1=0
    counter2=0
    for j in range(len(A)):
        counter1+=A[j][i]
        counter2+=A[i][j]
        sumn += A[i][j]
    sum_count+=counter1
    print('Сумма', i, '-ой строки:', counter1)
print('Сумма всех эллементов: ',sumn)

if sumn!=sum_count or counter1!=counter2:
    print('Не является магическим квадратом!!!')
else:
    print('Является магическим квадратом!!!')

for i in range(n):
    for j in range(n):
        print(A[i][j],end='   ')
    print()



#вторая часть
from random import *

N = int(input('Введите размер матрицы(NxN):'))
A = []
for i in range(N):
    B = []
    for j in range(N):
        B.append(randint(0, 10))
    A.append(B)

print('\nИсходная матрица: ')
for i in range(N):
    for j in range(N):
        print(A[i][j], end='   ')
    print()

for i in range(N):
    zamena = A[i][0]
    A[i][0] = A[i][N - 1]
    A[i][N - 1] = zamena
print('\nИзменённая матрица:')
for i in range(N):
    for j in range(N):
        print(A[i][j], end='   ')
    print()