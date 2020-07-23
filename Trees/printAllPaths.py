class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right

def printPaths(root,path):
        if root is None:
                return
        path.append(root.key)
        if not root.left and not root.right:
                #if leaf node then print the path
                print(path)
        printPaths(root.left,path)
        printPaths(root.right,path)
        path.pop()
        



root1 = Node(9)
root1.left = Node(8)
root1.right = Node(9)
root1.left.left = Node(5)
root1.left.right = Node(6)
root1.right.left = Node(3)
root1.right.right=Node(2)

path = []
printPaths(root1,path)
