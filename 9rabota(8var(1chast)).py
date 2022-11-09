file = open('/home/zloy/Рабочий стол/Progromice/Практики языки программирования /Практические работы /OzerovSS_ub23_vvod(1variant(1chast)).txt','r')
A=[]
z = 0
counter = 0

for line in file:
    s=line

    l = list(map(int, s.split()))
    
    A.append(l)
    
print(A)

n=len(A)
m=len(A)
for i in range (n):
    for j in range (m):
        print(A[i][j], end="   ")
    print()

for i in range(n):
    for j in range(m):
        if i<j:
            if A[i][j]>0:
                z+=1
                counter += A[i][j]
print('Число положительных эллементов над главной диагональю: ', z, '\nСумма положительных эллементов над диагональю:',counter)

file.close()



file1 = open('/home/zloy/Рабочий стол/Progromice/Практики языки программирования /Практические работы /OzerovSS_ub23_vivod(1variant(1chast)).txt', 'w')

print(file1.write(str("Число положительных эллементов над диагональю: ")))

print(file1.write(str(z)))

print(file1.write(str("\nСумма положительных эллементов над диагональю: ")))

print(file1.write(str(counter)))

print(file1.write(str("\nМассив: \n")))

print(file1.write(str(A)))

file1.close()














