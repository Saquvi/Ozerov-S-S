file = open('/home/zloy/Рабочий стол/Progromice/Практики языки программирования /Практические работы /OzerovSS_ub23_vvod(2variant(2 chast)).txt')

A=[]
B=[] 
C=[]
for line in file:
    s=line
    l=list(map(int, s.split()))
    A.append(l)


n = len(A)

m = len(A)

print("Исходная матрица: ")


for i in range(n):
    for j in range(m):
        print(A[i][j], end = "   ") 
    print()

for i in range(n):
    zamena = A[i][0]
    A[i][0] = A[i][n - 1]
    A[i][n - 1] = zamena
print('\nИзменённая матрица:')
for i in range(n):
    for j in range(m):
        print(A[i][j], end='   ')
        B.append(A[i][j])
    print()

file.close()


file1 = open('/home/zloy/Рабочий стол/Progromice/Практики языки программирования /Практические работы /OzerovSS_ub23_vivod(2variant(2chast)).txt', 'w')

print(file1.write(str('Изменённая матрица: \n')))

print(file1.write(str(A)))

file1.close()

