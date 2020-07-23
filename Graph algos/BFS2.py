from collections import defaultdict,deque

class graph:
        def __init__(self,V):
                self.V = V
                self.adj = defaultdict(list)
                self.setData()

        def setData(self):
                e = int(input("enter number of edges : "))
                for i in range(e):
                        print("enter source and dest : ",end="")
                        src,dest = map(int,input().split())
                        self.adj[src].append(dest)
                        self.adj[dest].append(src)

        def BFS(self,src,visited):
                visited[src]=True
                q = deque()
                q.append(src)
                while q:
                        u = q.popleft()
                        print(u,end=" ")
                        for v in self.adj[u]:
                                if not visited[v]:
                                        visited[v]=True
                                        q.append(v)
                                        
                
V = int(input("enter number of vertices : "))      
g = graph(V)
print("BFS traversal is : ")
visited=[False]*V
for i in range(V):
        if not visited[i]:
                g.BFS(i,visited)
