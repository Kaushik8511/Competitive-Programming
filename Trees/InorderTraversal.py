class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right

def InOrder(root):
        if root is None:
                return
        InOrder(root.left)
        print(root.key,end = " ")
        InOrder(root.right)

root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.left.left = Node(10)
root1.left.right = Node(10)
root1.right.left = Node(30)

InOrder(root1)
