def sm(n):
    l = list(map(int,list(str(n))))
    s = 0
    for i in l:s+=(i*i)
    return s

def happy(n):
    if n==1:return True
    if n==4:return False
    return happy(sm(n))

def isprime(n):
    if n<2:return False
    if n==2:return True
    if n&1==0:return False
    i=3
    while i*i<=n:
        if n%i==0:return False
        i+=2
    return True

def solve(left,right,n):
    for i in range(left,right+1):
        if isprime(i) and happy(i):
            n-=1
            print(i,end=" ")
            if n==0:
                print("\nResult",i)
                return
    print("No number is present at this index")

try:
    left = int(input())
    right = int(input())
    n = int(input())
    if left<=0 or left>right or n<=0:
        raise Exception()   
    solve(left,right,n)
except:print("invalid input")
