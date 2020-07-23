class vertex:
    def __init__(self):
        self.name = None
        self.next = None

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
def print_adjucent(head):
    current = head.next
    while current:
        print(current.name,end=' ')
        current = current.next
    print()
            

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
for i in range(n):
    print("adjucent to ",ver[i].name," are : ",end=' ' )
    print_adjucent(ver[i])


