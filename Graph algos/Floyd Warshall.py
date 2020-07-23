import collections
#edges = [[0,1,1],[0,2,6],[1,2,1],[1,3,4],[2,3,8]]
edges = [[0,1,5],[1,2,3],[2,3,1],[0,3,10]]
V = 4

def FW(V,edges):
    dist = [[float('inf') for _ in range(V)]for i in range(V)]
    for i in range(V):dist[i][i]=0
    for edge in edges:
        u,v,w = edge
        dist[u][v]=w
        #dist[v][u]=w


    for i in range(V):
        for j in range(V):
            for k in range(V):
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]

    return dist

dist = FW(V,edges)
for i in dist:print(i)
