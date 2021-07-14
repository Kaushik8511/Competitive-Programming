pascal = []
def cal_pascal(maximum):
    #change the value of mod according to question
    md = 10**9+7
    ln = len
    pascal.append([1,1])
    for i in range(1,maximum):
        temp=[1]
        for j in range(ln(pascal[-1])-1):
            #if there is a mod then cal using mod
            temp.append((pascal[-1][j]+pascal[-1][j+1])%md)
        temp.append(1)
        pascal.append(temp)
cal_pascal(1000)
def ncr(n,r):
    if n<=0 or r>n:return 0

    #if there is a mod then return res%p
    return pascal[n-1][r]

print(ncr(1000,25))
    
    
    
