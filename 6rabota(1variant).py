#первая часть
N=int(input("Введите длину массива:"))
x=[]
for i in range(N):
    print("Введите", i, "эллемент:")
    x.append(int(input()))
print("Массив:",x)
print ("Максимальный эллемент из массива:", max(x))
print("Массив в обратном порядке:", list(reversed(x)))
#вторая часть 
A=int(input("\nВведите длину массива:"))
z=[]
for i in range(A):
    print("Введите", i, "эллемент:")
    z.append(int(input()))
    srz=sum(z)/len(z)
    for i in range (len(z)):
        if z[i]==0:
            z[i]=srz
print("Массив:",z)
