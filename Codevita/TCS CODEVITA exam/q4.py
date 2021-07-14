from heapq import heappush,heappop

def solve(n,arr,k):
    sm = sum(arr)
    if k==0:return sm
    heap=[]
    #to implement max-heap we push -(actual value)
    for i in arr:heappush(heap,-i)
    for i in range(k):
        temp = -heappop(heap)
        #there is no positive value so we cant futher reduce sum
        if temp<=0:return sm
        temp1 = temp//2
        sm+=(temp1-temp)
        heappush(heap,-temp1)
    return sm


n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(solve(n,arr,k),end="")
