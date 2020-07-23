class vertex:
	def __init__(self):
		self.name=None
		self.next=None
		self.color=None

def adjucent(head,s):
#find adjucent vertices of a vertex
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

def find_color(head,active):
	current = active.next #first adjucent vertex
	col=[] #store color of all adjucent vertices
	while current:
		i=0
		temp=head
		while(current.name!=temp[i].name):
                        #find adj vertex in head array
			i += 1
		if temp[i].color==None:
                        #adj vertex is not colored yet
			current=current.next
			continue
		#adj vertex is colored so add color to col array
		col.append(temp[i].color)
		current = current.next
	c=0
	while(True):
		if c not in col:
			active.color=c
			break
		c+=1

n = int(input("enter how many vertices in your graph : "))
ver=[0 for i in range(n)]
print("enter name of vertices ===>")
s=[]
for i in range(n):
	ver[i]=vertex()
	ver[i].name=input("enter name of next vertex : ")
	s.append(ver[i].name)

print("enter adjucents of vertices ===>")
for i in range(n):
	adjucent(ver[i],s)
for i in range(n):
	find_color(ver,ver[i])
for i in range(n):
	print("color of vertex ",ver[i].name," is : ",ver[i].color)
