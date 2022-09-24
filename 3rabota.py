a=int(input())
x=int(input())
import math
if x==2 and a>5:
    y=x+a
elif x==2 and a<5:
    y=x-2
elif x>5 or a==5:
    y=x*a
else:
    y=math.pow(x,a)
print(y)
    
