file = open('/home/zloy/Рабочий стол/Progromice/Практики языки программирования /Практические работы /OzerovSS_ub23_vvod(1variant(2 chast)).txt')

A=[]

for line in file:
    s=line
    l=list(map(int, s.split()))
    A.append(l)


n = len(A)

m = len(A[0])

print("\nИсходный массив: ")

for i in range(n):
    for j in range(m):
        print(A[i][j], end = "   ")
    print()


for i in range(n):
    a_min = 0
    b_min = A[i][0]
    for j in range(m):
        if A[i][j] < b_min:
            a_min = j
            b_min = A[i][j]
    zam2 = A[i][0]
    A[i][0] = A[i][a_min]
    A[i][a_min] = zam2

for i in range(n):
    a_max = 0
    b_max = A[i][0]
    for j in range(m):
        if A[i][j] > b_max:
            a_max = j
            b_max = A[i][j]
    zam2 = A[i][m-1]
    A[i][m-1] = A[i][a_max]
    A[i][a_max] = zam2

print("\nИзмененный массив: ")
    
for i in range(n):
    for j in range(m):
        print(A[i][j], end = "   ")
    print()



file.close()

file1 = open('/home/zloy/Рабочий стол/Progromice/Практики языки программирования /Практические работы /OzerovSS_ub23_vivod(1variant(2chast)).txt', 'w')

print(file1.write(str("\nИзменённый массив: \n")))

print(file1.write(str(A)))

file1.close()