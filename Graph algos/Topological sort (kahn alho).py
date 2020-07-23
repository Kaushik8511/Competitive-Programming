from collections import defaultdict

class graph:
        def __init__(self,V,edges):
                self.V=V
                self.adj=defaultdict(list)
                self.indeg=[0]*V
                for i in edges:
                        src,dest=i
                        self.adj[src].append(dest)
                        self.indeg[dest]+=1

        def Topo(self):
                visited = []
                zero=[i for i in range(self.V) if self.indeg[i]==0]
                while zero:
                        u = zero.pop(0)
                        visited.append(u)
                        for i in self.adj[u]:
                                self.indeg[i]-=1
                                if self.indeg[i]==0:
                                        zero.append(i)
                for i in range(self.V):
                        if self.indeg[i]:
                                print("there is a cycle. Its not DAG")
                                return
                print(visited)

V=7
edges=[(0,1),(1,3),(1,5),(1,2),(2,4),(3,4),(4,6)]
g = graph(V,edges)
g.Topo()
