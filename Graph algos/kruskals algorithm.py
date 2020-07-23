import collections
V = 5
edges = [[0,1,5],[1,2,8],[0,2,6],[2,3,1],[2,4,8],[3,4,7]]

def kruskal(V,edges,start=0):
    edges.sort(key = lambda x:x[2])
    parent=[-1 for _ in range(V)]

    def find(u):
        while parent[u]!=-1:
            u=parent[u]
        return u
    def union(u,v):
        x,y = find(u),find(v)
        parent[x]=y
    n,MST = 0,[]
    i=0
    while n!=V-1:
       u,v,w = edges[i]
       if find(u)!=find(v):
           MST.append(edges[i])
           union(u,v)
           n+=1
       i+=1

    return MST
    


mst = kruskal(V,edges)
for edge in mst:
    u,v,w = edge
    print("edge",u,v,": weight",w)
