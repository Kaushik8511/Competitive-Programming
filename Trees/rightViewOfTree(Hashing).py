class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right
def printRight(root,level,d):
        if root is None:
                return
        d[level]=root.key#at each level it changes #of at that level times
        #and last time it changes at last node of level ie.preorder
        printRight(root.left,level+1,d)
        printRight(root.right,level+1,d)


def rightView(root):
        d = {}
        printRight(root,1,d)
        for i in sorted(d.keys()):
                print(d[i])



root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.right.left = Node(30)
root1.right.left.left = Node(10)
root1.left.right = Node(10)

rightView(root1)
