arr = [2,3,4,3,2,5,5]

def fun(arr):
    res=0
    for i in arr:res^=i
    return res

print(fun(arr))
