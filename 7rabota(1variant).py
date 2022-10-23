#Первая часть
import math 
def s(x,y,z):
    p=(x+y+z)/2
    s=math.sqrt(p*(p-x)*(p-y)*(p-z))
    return s 

A=[]
for i in range(1):
    print('Введите стороны треугольника:')
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    A.append(s(a,b,c))
for i in range(1):
    print('Площадь треугольника {:.2f}'.format(A[i]))



def S(x,y):
    S=x*y
    return S

B=[]
for i in range(1):
    print("Введите стороны прямоугольника: ")
    a=int(input("a:"))
    b=int(input("b:"))
    B.append(S(a,b))
for i in range(1):
    print('Площадь прямоугольника {:.2f}'.format(B[i]))
   
    
    
def Z(x):
    Z=(3*math.sqrt(3)*x**2)/2
    return Z 

C=[]
for i in range (1):
    print("Введите длину стороны правильного шестиугольника:")
    a=int(input('a:'))
    C.append(Z(a))
for i in range(1):
    print('Площадь правильного шестиугольника {:.2f}'.format(C[i]))




#вторая часть
from random import *
def trt(f):
    z=[randint(0,10) for i in range(f)]
    print(z) 
    print("Сумма эллементов:", sum(z))
    print('Среднее арифметическое:{0:.2f}'.format(sum(z)/len(z)))
    return f 
f=int(input("\nВведите длину первого массива(<15):"))
trt(f)
f=int(input("Введите длину второго массива(<15):"))
trt(f)
f=int(input("Введите длину третьего массива(<15):"))
trt(f)
