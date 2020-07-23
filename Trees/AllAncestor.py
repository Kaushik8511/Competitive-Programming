class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right

def printAllAncestors(root,x):
        if root is None:
                return False
        if root.key==x:
                return True
        left = printAllAncestors(root.left,x)
        right = False
        if not left:
                right = printAllAncestors(root.right,x)
        if left or right:
                print(root.key,end=" ")
        return left or right


root1 = Node(9)
root1.left = Node(8)
root1.right = Node(9)
root1.left.left = Node(5)
root1.left.right = Node(6)
root1.right.left = Node(3)
root1.right.right=Node(2)


printAllAncestors(root1,5)
