#it is BFS version , find odd cycle
from collections import defaultdict,deque

class graph:
        def __init__(self,V,edges):
                self.V = V
                self.adj = defaultdict(list)
                self.level=[0]*V
                for i in edges:
                        src,dest=i
                        self.adj[src].append(dest)
                        self.adj[dest].append(src)

        def isBBFS(self,s,visited):
                visited[s]=True
                q = deque()
                q.append(s)
                while q:
                        u = q.popleft()
                        for v in self.adj[u]:
                                if not visited[v]:
                                        visited[v]=True
                                        self.level[v]=self.level[u]+1
                                        q.append(v)
                                elif self.level[u]==self.level[v]:
                                        return False
                print(self.level)
                return True

                        


V=6
edges=[(0,1),(1,2),(2,3),(2,5),(3,4),(4,5)]
g = graph(V,edges)
visited=[False]*V
print(g.isBBFS(0,visited))
