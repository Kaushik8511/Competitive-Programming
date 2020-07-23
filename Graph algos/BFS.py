class vertex:
    def __init__(self):
        self.name = None
        self.next = None
        self.visited = False
        
def adjucent(head,s):
    current = head
    while(True):
        print("enter next adjucent to : (enter Z if no further adjucent)",head.name,end = ' : ')
        v = input()
        if(v in 'zZ'):
            return
        if(v not in s):
            print("something is wrong please check and reeenter name")
            continue
        current.next = vertex()
        current.next.name=v
        current = current.next
        
def find_adjucent(head,active,queue): 
    current = active.next
    while current:
        nm = current.name
        i=0
        temp = head
        while(nm!=temp[i].name):
            i += 1
        if temp[i].visited == False:
            queue.append(temp[i])
            temp[i].visited = True
        current = current.next

def BFS(head):
    queue = [head[0]]
    head[0].visited = True
    while len(queue)!=0:
        active = queue.pop(0)
        find_adjucent(head,active,queue)
        print(active.name,end=' ')

        
        

n = int(input("enter number of vertices in your graph : "))
ver = [0 for i in range(n)]
s=[]
for i in range(n):
    ver[i]=vertex()
    ver[i].name=input("enter name of next node : ")
    s.append(ver[i].name)

print("\n\nenter name of adjucent vertices")
for i in range(n):
    adjucent(ver[i],s)


BFS(ver)
