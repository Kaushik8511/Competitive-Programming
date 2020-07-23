def visit(source,pre,visited,result):
        visited[source-1]=True
        if source in pre:
                for i in pre[source]:
                        if not visited[i-1]:
                                visit(i,pre,visited,result)
        result.append(source)


n = int(input("enter number of vertices : "))
visited = [False for i in range(n)] #is visited or not
e = int(input("enter number of edges : "))
pre = {}#dict to store edges of graph
result=[]
for i in range(e):
        print("enter source and destination : ")
        s,d = map(int,input().split())
        if s not in pre:
                pre[s]=[d]
        else:
                pre[s].append(d)
for i in range(n):
        if not visited[i]:
                visit(i+1,pre,visited,result)
                print("call for : " ,i+1)
result.reverse()
print(result)
