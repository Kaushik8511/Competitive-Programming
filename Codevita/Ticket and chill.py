def check(n,mid,k,tic):
    prev = 0
    for i in range(n):
        if tic[i]+prev<=mid:
            prev = 0
            continue
        if prev>mid:return False
        more_tic_can_transfer = mid-prev
        temp = min(tic[i]-more_tic_can_transfer,k)
        temp = max(temp,0)
        if tic[i]-temp+prev>mid:return False
        prev = temp
    return prev==0

def bs(n,k,tic):
    start,end = 1,max(tic)
    res=-1
    while start<=end:
        mid = start+(end-start)//2
        temp = check(n,mid,k,tic)
        if temp:
            res=mid
            end = mid-1
        else:
            start=mid+1
    return res

n,k = map(int,input().split())
tickets = list(map(int,input().split()))
print(bs(n,k,tickets))
