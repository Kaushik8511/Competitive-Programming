def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)

        
a,b,c=map(int,input().split())
g = gcd(a,b)
if c%g==0:print("Yes")
else:print("No")
