import collections
arr = 'abdjfiasfbfajffff'
k = 3

def fun(arr,k):
    d = {}
    start=0
    res=[]
    for end in range(len(arr)):
        if arr[end] in d:d[arr[end]]+=1
        else:d[arr[end]]=1
        if end-start+1==k:
            res.append(len(d))
            d[arr[start]]-=1
            if d[arr[start]]==0:del d[arr[start]]
            start+=1
    return res

print(fun(arr,3))
