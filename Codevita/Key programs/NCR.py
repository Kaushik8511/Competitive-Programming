def ncr(n,r):
    if r>n :return 0
    if r==n:return 1
    f = [1 for i in range(n+1)]
    for i in range(2,n+1):f[i]=i*f[i-1]

    #if there is a mod then do mod first and then return answer    
    return f[n]//(f[n-r]*f[r])




print(ncr(50,25))
