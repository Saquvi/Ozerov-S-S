n=int(input())
fact=1 
s=0
for i in range(2,n+1):
    fact = fact *i  
    s=s+fact
print(s)
