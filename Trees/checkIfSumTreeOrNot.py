class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right

def isSumTree(root):
        if root is None:
                return 0
        if not root.left and not root.right:
                return root.key
        if root.key==isSumTree(root.left)+isSumTree(root.right):
                return 2*root.key
        return float('-inf')



root1 = Node(32)
root1.left = Node(11)
root1.right = Node(5)
root1.left.left = Node(5)
root1.left.right = Node(6)
root1.right.left = Node(3)
root1.right.right=Node(2)

if isSumTree(root1)!=float('-inf'):
        print(True)
else:
        print(False)
