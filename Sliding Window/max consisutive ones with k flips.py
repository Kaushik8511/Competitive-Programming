arr = [0,0,0,0,0,0,0,0,0,1,1,1]

def fun(arr,k):
    res = start = zero = 0
    for end in range(len(arr)):
        if arr[end]==0:zero+=1
        while zero>k:
            if arr[start]==0:zero-=1
            start+=1
        res=max(res,end-start+1)
    return res

print(fun(arr,3))
            
