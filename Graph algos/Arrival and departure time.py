from collections import defaultdict,deque

class graph:
        def __init__(self,V):
                self.V=V
                self.adj=defaultdict(list)
                self.arrival=[0]*V
                self.dept=[0]*V
                self.setData()

        def setData(self):
                e = int(input("enter number of edges : "))
                for i in range(e):
                        print("enter source and dest : ",end="")
                        src,dest=map(int,input().split())
                        self.adj[src].append(dest)
                        self.adj[dest].append(src)
        def DFS(self,s,visited,time):
                visited[s]=True
                time+=1
                self.arrival[s]=time
                for i in self.adj[s]:
                        if not visited[i]:
                                time=self.DFS(i,visited,time)
                time+=1
                self.dept[s]=time
                return time
        
        def printTime(self):
                for i in range(self.V):
                        print(i,self.arrival[i],self.dept[i])


V=int(input("enter number of vertices : "))
g = graph(V)
visited = [False]*V
for i in range(V):
        if not visited[i]:
                g.DFS(i,visited,0)
g.printTime()
