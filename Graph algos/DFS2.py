from collections import defaultdict,deque

class graph:
        def __init__(self,V):
                self.V=V
                self.adj=defaultdict(list)
                self.setData()

        def setData(self):
                e = int(input("enter number of edges : "))
                for i in range(e):
                        print("enter source and destination : ",end="")
                        src,dest = map(int,input().split())
                        self.adj[src].append(dest)
                        self.adj[dest].append(src)

        def DFS(self,s,visited):
                visited[s]=True
                print(s,end = " ")
                for i in self.adj[s]:
                        if not visited[i]:
                                self.DFS(i,visited)

V = int(input("enter number of vertices : "))
g = graph(V)
visited = [False]*V
for i in range(V):
        if not visited[i]:
                g.DFS(i,visited)
