class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right

def isIdentical(root1,root2):
        if root1 is None and root2 is None:
                return True
        if root1 is None or root2 is None:
                return False

        return (root1.key==root2.key)and isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)

root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.left.left = Node(10)
root1.left.right = Node(10)
root1.right.left = Node(30)


root2 = Node(20)
root2.left = Node(30)
root2.right = Node(20)
root2.left.left = Node(10)
root2.right.right = Node(10)
root2.right.left = Node(30)

print(isIdentical(root1,root2))
