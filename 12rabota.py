#первая часть 
from random import *
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

def f(X,N):
    return X**N/fac(N)


z=randint(0,20)
c=randint(0,20)
print("Ответ: {0:.2f}".format(f(z,c))) 





#вторая часть
def rec():
    a = int(input("Введите число(последний ноль прервет цикл): "))
    if a == 0:
        return 0
    else:
        return max(a, rec())

print('Наибольшее число: ', rec())