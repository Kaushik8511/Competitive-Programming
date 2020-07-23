def C(n,k):
    ans = 1
    for i in range(n,n-k,-1):
        ans*=i
    for i in range(2,k+1):
        ans//=i
    return ans

def catalan(n):
    if n<=1:return 1

    ans = C(2*n,n)
    return ans//(n+1)

print(catalan(9))
