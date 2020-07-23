arr = [4,5,3,6,3,6,7,5,4,5,7,1,2,4,6,7,5,4,6,13]
sm = 45

def fun(arr,k):
    sm=start=0
    mn = float('inf')
    for end in range(len(arr)):
        sm+=arr[end]
        while start<=end and sm>=k:
            mn = min(mn,end-start+1)
            sm-=arr[start]
            start+=1
    return mn

print(fun(arr,sm))
