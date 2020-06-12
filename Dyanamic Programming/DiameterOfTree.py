class Node:
        def __init__(self,name):
                self.left=None
                self.right=None
                self.name=name
class Tree:
        def __init__(self):
                self.root=None
                
def createTree():
        name = input("enter name of node (enter Z if no further node)")
        if name in "Zz":
                return
        root = Node(name)
        print("enter left tree of ",name," : ")
        root.left = createTree()
        print("enter right of : ",name)
        root.right = createTree()
        return root

def diameterOfTree(root):
        if root==None:
                return 0
        l = diameterOfTree(root.left)
        r = diameterOfTree(root.right)

        temp = max(l,r)+1
        ans = max(temp,l+r+1)
        global res
        res=max(res,ans)
        return temp


t = Tree()
t.root = createTree()
res=0
diameterOfTree(t.root)
print(res)

