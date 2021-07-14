prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def find_prime(left,right):
    start,end = 0,len(prime)-1
    while start<=end and prime[start]<left:start+=1
    while end>=start and prime[end]>right:end-=1
    return prime[start:end+1]

def isPrime(n):
    if n<2:return False
    if n==2:return True
    if n&1==0:return False
    i=3
    while i*i<=n:
        if n%i==0:return False
        i+=2
    return True


def combination(prm):
    ret = set()
    for i in range(len(prm)):
        for j in range(len(prm)):
            if i!=j:
                temp = int(str(prm[i])+str(prm[j]))
                if isPrime(temp):
                    ret.add(temp)
    return list(ret)

def fib(a,b,n):
    if n==1:return a
    if n==2:return b
    for i in range(3,n+1):
        res = a+b
        a = b
        b = res
    return res

def solve(left,right):
    prm = find_prime(left,right)
    comb = combination(prm)
    a = min(comb)
    b = max(comb)
    n = len(comb)
    print(fib(a,b,n))
    


left,right = map(int,input().split())
solve(left,right)
