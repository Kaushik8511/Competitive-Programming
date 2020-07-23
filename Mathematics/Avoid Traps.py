prime = [1 for i in range(100001)]

def sieve():
    n = len(prime)-1
    prime[0]=0
    prime[1]=0
    i=2
    while(i*i<=n):
        if prime[i]==1:
            j=i*i
            while(j<=n):
                prime[j]=0
                j+=i
        i+=1
    for i in range(1,len(prime)):
        prime[i]=prime[i]+prime[i-1]

sieve()


def isspecial(i,x):
    if (prime[i]/i)>=x:
        return True
    return False


curr = 0
ans = 0
f=True
print("enter r1,r2")
r1,r2=map(int,input().split())
print("enter string")
s = input()
n = len(s)

while(curr!=n-1):
        jump = -1
        if curr+1<n and s[curr+1]=="#":
            jump=1
        if curr+2<n and s[curr+2]=="#":
            jump = 2
        if isspecial(curr+1,r1/r2):
            A = prime[curr+1]
            if A>jump and curr+A<n and s[curr+A]=="#":
                jump = A
        if jump==-1:
            f=False
            print("No way")
            break
        ans+=1
        curr+=jump
if f:
    print(ans)
