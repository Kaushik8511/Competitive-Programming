import collections
V = 5
edges = [[0,1,5],[1,2,8],[0,2,6],[2,3,1],[2,4,8],[3,4,7]]

def prim(V,edges,start):
    graph = collections.defaultdict(list)
    w = {}
    for edge in edges:
        u,v,wt = edge
        graph[u].append(v)
        graph[v].append(u)
        w[u,v]=w[v,u]=wt
    
    key = [float('inf') for _ in range(V)]
    key[start]=0
    parent = [None for _ in range(V)]
    visited = [False for _ in range(V)]
    visited[start]=True

    q = collections.deque()
    q.append(start)
    while q:
        curr=q.popleft()
        for adj in graph[curr]:
            if key[adj]>w[curr,adj]:
                key[adj]=w[curr,adj]
                parent[adj]=curr
            if not visited[adj]:
                visited[adj]=True
                q.append(adj)
    return parent,key

parent,wts = prim(V,edges,0)
for i in range(1,len(parent)):
    print("edge",i,parent[i],": weight",wts[i])
