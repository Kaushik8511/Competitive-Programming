class vertex:
    def __init__(self):
        self.name=None
        self.next=None
        self.parent=None
        self.visited=False
        self.depth=None


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
        
def find_adjucent(head,active,queue,depth):
    current = active.next
    while current:
        nm = current.name
        i=0
        temp = head
        while(nm!=temp[i].name):
            i += 1
        if temp[i].visited == False:
            temp[i].parent=active
            temp[i].depth=depth
            queue.append(temp[i])
            temp[i].visited = True
        current = current.next

def find_parent(head):
    queue = [head[0]]
    head[0].visited = True
    depth=0
    head[0].depth=depth
    depth += 1
    while len(queue)!=0:
        active = queue.pop(0)
        find_adjucent(head,active,queue,depth)
        depth += 1






n = int(input("enter how many vertices in your graph : "))
print("\nenter name of vertices => ")
ver = [0 for i in range(n)]
s=[]
for i in range(n):
    ver[i]=vertex()
    ver[i].name=input("enter name of next vertex : ")
    s.append(ver[i].name)

print("\n\nenter name of adjucent vertices")
for i in range(n):
    adjucent(ver[i],s)
find_parent(ver)
for i in range(n):
    if ver[i].parent == None:
        print("parent of vertex ",ver[i].name," is : None and depth is : ",ver[i].depth)
        continue
    print("parent of vertex ",ver[i].name," is : ",ver[i].parent.name,"and depth is : ",ver[i].depth)
