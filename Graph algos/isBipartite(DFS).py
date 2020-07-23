#using 2 colorable problem
from collections import defaultdict

class graph:
        def __init__(self,V,edges):
                self.V=V
                self.adj=defaultdict(list)
                for i in edges:
                        src,dest = i
                        self.adj[src].append(dest)
                        self.adj[dest].append(src)

        def isBDFS(self,s,visited,color):
                for u in self.adj[s]:
                        if not visited[u]:
                                visited[u]=True
                                color[u]=not color[s]
                                if not self.isBDFS(u,visited,color):
                                        return False
                        elif color[s]==color[u]:
                                return False
                return True


V=6
edges=[(0,1),(1,2),(2,3),(2,5),(3,4),(4,5)]
g = graph(V,edges)
visited=[False]*V
color = [None]*V
print(g.isBDFS(0,visited,color))
