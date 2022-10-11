#первая часть 
n=int(input("Введите длину массива:"))
y=[]
for i in range(n):
    print("Введите", i, "эллемент:")
    y.append(int(input()))
print("Минимальный эллемент из массива",min(y))
minindex=y.index(min(y))
print("Индекс минимального эллемента", minindex) 

#вторая часть 
a=int(input("\nВведите длину массива:"))
z=[]
x=[]
c=[]
for i in range (a):
    print ("Введите", i, "эллемент",end=" ")
    z.append(int(input("(не забудь про отрицательные числа):\n")))
for i in range(a):
    if z[i]>=0:
        x.append(z[i])
for i in range(a):
    if z[i]<0:
        c.append(z[i])
print(z)
print(x)
print(c)
