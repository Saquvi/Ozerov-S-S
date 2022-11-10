file = open('/home/zloy/Рабочий стол/Progromice/Практики языки программирования /Практические работы /OzerovSS_ub23_vvod(2variant(1chast)).txt')
A=[] 
sumn = 0
for line in file:
    s=line 
    l=list(map(int, s.split()))
    A.append(l)

n = len(A)

m= len(A)

print("Исходный массив: ")

for i in range (n):
    for j in range(m):
        print(A[i][j], end = "   ")
    print() 

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

file.close()


file1 = open('/home/zloy/Рабочий стол/Progromice/Практики языки программирования /Практические работы /OzerovSS_ub23_vivod(2variant(1chast)).txt', 'w')

print(file1.write(str("Исходный массив: \n ")))

print(file1.write(str(A)))

for i in range (len(A)):
    counter1=0
    for j in range(len(A)):
        counter1+=A[j][i]
    print(file1.write(str('\nСумма строки №  ')))
    print(file1.write(str(i)))
    print(file1.write(str('   =    ')))
    print(file1.write(str(counter1)))

print(file1.write(str('\nСумма всех эллементов: ')))

print(file1.write(str(sumn)))

if sumn!=sum_count or counter1!=counter2:
    print(file1.write(str('\nНе является магическим квадратом!!!')))
else:
    print(file1.write(str('\nЯвляется магическим квадратом!!!')))

file1.close()