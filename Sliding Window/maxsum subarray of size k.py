arr = [10,30,2,8,4,5,3,5,3,5,7,6,5,3,2,6,37]

def fun(arr,k):
    if len(arr)<k:return 0
    temp = sm = sum(arr[:k])
    start=0
    for i in range(1,len(arr)-k+1):
        temp = temp-arr[i-1]+arr[i+k-1]
        if temp>sm:
            sm=temp
            start=i

    return arr[start:start+k]
print(fun(arr,3))
