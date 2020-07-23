class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right
def mirror(x,y):
        if x is None and y is None:
                return True
        if x is None or y is None:
                return False
        return mirror(x.left,y.right)and mirror(x.right,y.left)


def isSymmetry(root):
        return mirror(root.left,root.right)


root1 = Node(9)
root1.left = Node(8)
root1.right = Node(9)
root1.left.left = Node(5)
root1.left.right = Node(6)
root1.right.left = Node(3)
root1.right.right=Node(2)


print(isSymmetry(root1))
