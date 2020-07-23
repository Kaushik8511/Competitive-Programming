class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right

class NodeInfo:
        def __init__(self,key=None,level=None,parent=None):
                self.key=key
                self.level=level
                self.parent=parent
def Inorder(root,level,parent,n1,n2):
        if root is None:
                return
        Inorder(root.left,level+1,root,n1,n2)
        if n1.key==root.key:
                n1.parent=parent
                n1.level=level
        if n2.key==root.key:
                n2.parent=parent
                n2.level=level
        Inorder(root.right,level+1,root,n1,n2)
        


def check_cousins(root,x,y):
        if root is None:
                return
        n1 = NodeInfo(x,1,None)
        n2 = NodeInfo(y,1,None)
        Inorder(root,1,None,n1,n2)
        if n1.level==n2.level and n1.parent!=n2.parent:
                return True
        return False


root1 = Node(20)
root1.left = Node(30)
root1.right = Node(21)
root1.left.left = Node(4)
root1.left.right = Node(11)
root1.right.right = Node(5)
root1.right.left=Node(12)

print(check_cousins(root1,4,12))
