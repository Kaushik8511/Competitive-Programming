from collections import defaultdict

class graph:
        def __init__(self,V,edges):
                self.V=V
                self.adj=defaultdict(list)
                for i in edges:
                        src,dest=i
                        self.adj[src].append(dest)
                        self.adj[dest].append(src)

        def DFS(self,s,visisted,parent):
                visisted[s]=True
                for i in self.adj[s]:
                        if not visited[i]:
                                self.DFS(i,visited,s)
                        elif i!=parent:
                                return True
                return False

V=3
visited=[False]*3
edges=[(0,1),(1,2)]
g=graph(V,edges)
print(g.DFS(0,visited,-1))
