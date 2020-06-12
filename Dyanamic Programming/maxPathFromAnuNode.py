class Node:
        def __init__(self,value):
                self.left=None
                self.right=None
                self.value=value
class Tree:
        def __init__(self):
                self.root=None
                
def createTree():
        value = int(input("enter value of node (enter Z if no further node)"))
        if value==-1:
                return
        root = Node(value)
        print("enter left of ",value," : ")
        root.left = createTree()
        print("enter right of : ",value)
        root.right = createTree()
        return root

def MaxPath(root):
        if root==None:
                return 0
        l = MaxPath(root.left)
        r = MaxPath(root.right)

        temp = max(max(l,r)+root.value,root.value)
        ans = max(temp,l+r+root.value)
        global res
        res = max(res,ans)
        return temp



t = Tree()
t.root = createTree()
res=0
MaxPath(t.root)
print(res)

