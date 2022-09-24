import math
x=float(3.251)
y=float(0.325)
z=float(0.466*math.pow(10,-4))
s=math.pow(2,y)+math.pow(math.pow(3,x),y)-((y*(math.atan(z)-1/3))/(math.fabs(x)+(1/math.pow(y,2)+1)))
print("s= {0:.2f}".format(s))
