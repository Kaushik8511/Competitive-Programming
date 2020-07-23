import collections
edges = [[0,1,1],[0,2,6],[1,2,1],[1,3,4],[2,3,8]]
V = 4

def dijstra(V,e,s):
    g = collections.defaultdict(list)
    w = {}
    for edge in e:
        g[edge[0]].append(edge[1])
        g[edge[1]].append(edge[0])
        w[edge[0],edge[1]]=w[edge[1],edge[0]]=edge[2]
    dist = [float('inf') for i in range(V)]
    dist[s]=0
    q = collections.deque()
    q.append(s)
    visited = [False for i in range(V)]
    visited[s]=True
    while q:
        curr = q.popleft()
        for adj in g[curr]:
            if w[curr,adj]+dist[curr]<dist[adj]:
                dist[adj]=w[curr,adj]+dist[curr]
            if not visited[adj]:
                visited[adj]=True
                q.append(adj)
    return dist

s = 0
print("source is ",s)
dist = dijstra(V,edges,s)
for i in range(V):
    print(i,dist[i])
        
    
