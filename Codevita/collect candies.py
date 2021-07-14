from heapq import heappush,heappop

def solve(n,c):
    res = 0
    while len(c)!=1:
        n1 = heappop(c)
        n2 = heappop(c)
        res+=n1+n2
        heappush(c,n1+n2)
    return res


n = int(input())
candies = list(map(int,input().split()))
print(solve(n,candies))
