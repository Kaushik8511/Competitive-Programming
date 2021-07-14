import  collections

def solve(n,g,indeg,time):
    res = [0 for _ in range(n)]
    zero = [i+1 for i in range(n) if indeg[i]==0]
    
    while zero:
        curr = zero.pop()
        res[curr-1]+=time[curr-1]
        for adj in g[curr]:
            indeg[adj-1]-=1
            if indeg[adj-1]==0:zero.append(adj)
            res[adj-1]=max(res[adj-1],res[curr-1])
    print(res)
    return max(res)

t = int(input())
while t:
    n = int(input())
    g = collections.defaultdict(list)
    indeg = [0 for _ in range(n)]
    time = [0 for _ in range(n)]
    for i in range(n):
        arr = list(map(int,input().split()))
        v = arr[0]
        time[v-1]=arr[1]
        for u in arr[2:]:
            if u>0:
                g[u].append(v)
                indeg[v-1]+=1
    print(solve(n,g,indeg,time))     
        
    
    t-=1
