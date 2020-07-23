class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right

def PostOrder(root):
        if root is None:
                return
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.key,end=" ")

root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.left.left = Node(10)
root1.left.right = Node(10)
root1.right.left = Node(30)

PostOrder(root1)
