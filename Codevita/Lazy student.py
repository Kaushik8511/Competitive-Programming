def gcd(n1,n2):
    if n2==0:return n1
    return gcd(n2,n1%n2)

pascal = []
def cal_pascal(maximum):
    md = 10**9+7
    ln = len
    pascal.append([1,1])
    for i in range(1,maximum+1):
        temp = [1]
        for j in range(ln(pascal[-1])-1):
            temp.append((pascal[-1][j]+pascal[-1][j+1])%md)
        temp.append(1)
        pascal.append(temp)
        
cal_pascal(1000)
print(len(pascal))
def ncr(n,r):
    return pascal[n-1][r]



def solve(n,m,t):
    if n-m<t:
        print(1)
        return
    if m==0:
        print(0)
        return
    md = 10**9+7
    print("nm",n-m,t)
    p = ncr(n-m,t)
    q = ncr(n,t)
    print("fail",p,q)
    g = gcd(p,q)
    p //= g
    q//=g
    p = q-p
    p = p%md
    print(p,q)
    q = pow(q,md-2,md)
    print((p*q)%md)    


n,m,t = map(int,input().split())
solve(n,m,t)
