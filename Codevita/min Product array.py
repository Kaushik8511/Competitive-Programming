def solve(arr1,arr2,n,k):
    os = 0
    for i in range(n):os+=(arr1[i]*arr2[i])
    res = os
    for i in range(n):
        old = arr1[i]*arr2[i]
        new = min((arr1[i]+2*k)*arr2[i],(arr1[i]-2*k)*arr2[i])
        temp_prod = os-old+new
        res = min(res,temp_prod)
    return res



n,k = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(solve(arr1,arr2,n,k))
