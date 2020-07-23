from collections import defaultdict,deque

class graph:
        def __init__(self,V,edges):
                self.V=V
                self.adj=defaultdict(list)
                for i in edges:
                        src,dest=i
                        self.adj[src].append(dest)
                        self.adj[dest].append(src)

        def BFS(self,s,visited):
                visited[s]=True
                q=deque()
                q.append((s,-1))
                while q:
                        u,parent = q.popleft()
                        for v in self.adj[u]:
                                if not visited[v]:
                                        visited[v]=True
                                        q.append((v,u))
                                elif v!=parent:
                                        return True
                return False
v=4
edges=[(0,1),(1,2),(2,3)]
visited=[False]*v
g=graph(v,edges)
print(g.BFS(0,visited))
