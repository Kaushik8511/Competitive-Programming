class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right
def LevelOrder(root):
        if root is None:
                return
        queue = [root]
        while queue:
                curr = queue.pop(0)
                print(curr.key,end=" ")
                if curr.left:
                        queue.append(curr.left)
                if curr.right:
                        queue.append(curr.right)


root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.right.right = Node(10)
root1.left.right = Node(10)
root1.right.left = Node(30)

LevelOrder(root1)
