class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right

def RLevelOrder(root):
        if root is None:
                return
        q = [root]
        s = []
        while q:
                curr = q.pop(0)
                s.append(curr.key)
                if curr.right:
                        q.append(curr.right)
                if curr.left:
                        q.append(curr.left)
        s.reverse()
        for i in s:
                print(i,end=" ")


root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.left.left = Node(10)
root1.left.right = Node(10)
root1.right.left = Node(30)

RLevelOrder(root1)
