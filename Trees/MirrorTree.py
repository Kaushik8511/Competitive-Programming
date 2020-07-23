class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right
def InOrder(root):
        if root is None:
                return
        InOrder(root.left)
        print(root.key,end=" ")
        InOrder(root.right)
                
def swap(root):
        if root is None:
                return
        temp = root.left
        root.left = root.right
        root.right = temp


def Mirror(root):
        if root is None:
                return
        Mirror(root.left)
        Mirror(root.right)
        swap(root)
        




root1 = Node(9)
root1.left = Node(8)
root1.right = Node(9)
root1.left.left = Node(5)
root1.left.right = Node(6)
root1.right.left = Node(3)
root1.right.right=Node(2)


InOrder(root1)
print()
Mirror(root1)
InOrder(root1)
