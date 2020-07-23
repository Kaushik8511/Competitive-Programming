class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right
def printleft(root,level,d):
        if root is None:
                return
        if level not in d:
                d[level]=root.key
        printleft(root.left,level+1,d)
        printleft(root.right,level+1,d)

def leftView(root):
        d = {}
        printleft(root,1,d)
        for i in d:
                print(d[i],end = " ")


root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.right.left = Node(30)
root1.right.left.left = Node(10)
root1.left.right = Node(10)


leftView(root1)
