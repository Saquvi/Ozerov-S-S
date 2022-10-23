#первая часть 
import math 
def s(x,y):
    c=math.sqrt(x**2+y**2)
    h=(x*y)/c
    s=1/2*(c*h)
    return s 

A=[]
for i in range(1):
    print("Введите стороны прямоугольного треугольника:")
    X=int(input('X:'))
    Y=int(input('Y:'))
    A.append(s(X,Y))
for i in range(1):
    print('Площадь прямоугольного треугольника {:.2f}'.format(A[i]))
    
   
    
def z(x,y):
    z=x*y 
    return z 

B=[]
for i in range(1):
    print("Введите стороны прямоугольника:")
    X=int(input('X:'))
    Y=int(input('Y:'))
    B.append(z(X,Y))    
for i in range(1):
    print('Площадь прямоугольника {:.2f}'.format(B[i]))
#торая часть
x = int(input('\nВведите число в 10-ой системе:'))
y = oct(x)[2:]
print('Число ' ,x,' в 8-ой системе:','0' * (10 - len(y)), y,sep='')
