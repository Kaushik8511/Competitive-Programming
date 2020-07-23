class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right
def PreOrder(root):
        if root is None:
                return
        print(root.key,end = " ")
        PreOrder(root.left)
        PreOrder(root.right)


root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.left.left = Node(10)
root1.left.right = Node(10)
root1.right.left = Node(30)

PreOrder(root1)
