class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right
#using level order traversal
#idea is to make level order traversal and print node if its a last node of level
def rightView(root):
        if root is None:
                return
        q = [root]
        while q:
                s=len(q)
                i=0
                while i<s:
                        i+=1
                        curr = q.pop(0)
                        if i==s:#last node of current level
                                print(curr.key)
                        if curr.left:
                                q.append(curr.left)
                        if curr.right:
                                q.append(curr.right)
                                

root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.right.left = Node(30)
root1.right.left.left = Node(10)
root1.left.right = Node(10)

rightView(root1)
