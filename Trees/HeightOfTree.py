class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right

def height(root):
        if root is None:
                return 0
        return 1+max(height(root.left),height(root.right))


root1 = Node(20)
root1.left = Node(30)
root1.left.left = Node(20)
root1.left.left.left = Node(10)
root1.left.left.left.left = Node(10)
root1.left.left.left.left.left = Node(30)

print(height(root1))
