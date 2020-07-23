class vertex:
	def __init__(self):
		self.name=None
		self.parent=None

class edge:
	def __init__(self):
		self.source=None
		self.dest=None
		self.weight=None

def sort_edge(ed):
	for i in range(1,len(ed)):
		j=i
		temp=ed[i]
		while(j>0 and ed[j-1].weight>temp.weight):
			ed[j]=ed[j-1]
			j-=1
		ed[j]=temp

def find(ver,a):
	i=0
	while ver[i].name!=a:
		i+=1
	ptr=ver[i]
	while ptr.parent:
		ptr=ptr.parent
	return ptr.name

def uniona(ver,a,b):
	i=0
	while ver[i].name!=a:
		i+=1
	ptr1=ver[i]
	i=0
	while ver[i].name!=b:
		i+=1
	ptr2=ver[i]
	while ptr1.parent:
		ptr1=ptr1.parent
	while ptr2.parent:
		ptr2=ptr2.parent
	ptr1.parent=ptr2

n=int(input("enter how many vertices in your graph : "))
print("enter name of vertices ===>")
ver=[0 for i in range(n)]
s=[]
for i in range(n):
	ver[i]=vertex()
	ver[i].name=input("enter name of vertex : ")
	s.append(ver[i].name)
e=int(input("enter how many edges in your graph : "))
ed=[0 for i in range(e)]
i=0
while i<e:
	ed[i]=edge()
	ed[i].source=input("enter source of next edge : ")
	ed[i].dest=input("enter destination of next edge : ")
	if ed[i].source not in s or ed[i].dest not in s:
		print("something went wrong please check and reenter names of source and destination")
		continue
	ed[i].weight=int(input("enter weight of next edge : "))
	i+=1
sort_edge(ed)

mst=[]
for i in range(e):
	if find(ver,ed[i].source) != find(ver,ed[i].dest):
		mst.append(ed[i])
		uniona(ver,ed[i].source,ed[i].dest)

print("\nedges in the minimal spanning tree ===>")
for i in mst:
	print("SOURCE : ",i.source,"  DESTINATION",i.dest,"  WEIGHT",i.weight)