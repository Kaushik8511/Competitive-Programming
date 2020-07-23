from collections import defaultdict

class graph:
        def __init__(self,V,edges):
                self.V=V
                self.adj=defaultdict(list)
                for i in edges:
                        src,dest=i
                        self.adj[src].append(dest)
        def DFS(self,s,visited,dept,time):
                visited[s]=True
                time+=1
                for i in self.adj[s]:
                        if not visited[i]:
                                time = self.DFS(i,visited,dept,time)
                time+=1
                dept[time]=s
                return time

V=6
visited=[False]*V
dept={}
edges=[(0,1),(1,3),(1,5),(1,2),(2,4),(3,4)]
g = graph(6,edges)
g.DFS(0,visited,dept,0)
for i in sorted(dept.keys(),reverse=True):
        print(dept[i],end=" ")
