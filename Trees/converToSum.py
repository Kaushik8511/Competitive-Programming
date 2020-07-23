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


def convertToSum(root):
        if root is None:
                return 0
        l = convertToSum(root.left)
        r = convertToSum(root.right)

        old = root.key
        if root.left or root.right:
                root.key = l+r
        return root.key+l+r


root1 = Node(9)
root1.left = Node(8)
root1.right = Node(9)
root1.left.left = Node(5)
root1.left.right = Node(6)
root1.right.left = Node(3)
root1.right.right=Node(2)

convertToSum(root1)
InOrder(root1)
