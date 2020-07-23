n = int(input("enter how many vertices your graph have : "))
visited = {}
adjecent = {}
ver = []
print("enter names")
for i in range(n):
    ver.append(input())
    visited[ver[i]]=False
e = int(input("how many edges in your graph : "))
for i in range(e):
    print("enter source and destination of edge : ")
    s = input()
    d = input()
    if s not in adjecent:
        adjecent[s]=[d]
    else:
        adjecent[s].append(d)
    if d not in adjecent:
        adjecent[d]=[s]
    else:
        adjecent[d].append(s)
def DFS(a):
    print(a,end='  ')
    visited[a]=True
    if a in adjecent:
        for i in adjecent[a]:
            if not visited[i]:
                DFS(i)
DFS(ver[0])
