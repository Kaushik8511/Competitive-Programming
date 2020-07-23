import collections
edges = [[0,1,1],[0,2,6],[1,2,1],[1,3,4],[2,3,8]]
V = 4

def BF(V,edges,s):
    dist = [float('inf') for _ in range(V)]
    dist[s] = 0
    parent = [None for _ in range(V)]

    for i in range(V-1):
        for edge in edges:
            u,v,w=edge
            if dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
                parent[v]=u
            if dist[v]+w<dist[u]:
                dist[u]=dist[v]+w
                parent[u]=v
            

    for edge in edges:
        u,v,w=edge
        if dist[u]+w<dist[v] or dist[v]+w<dist[u]:
            print("negative weight cycle")
            return None,None

    return dist,parent

s = 3
print("source is",s)
dist,parent = BF(V,edges,s)
if dist:
    for i in range(V):
        print("vertex",i,"distance",dist[i],"parent",parent[i])
