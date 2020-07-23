class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right = right
def SpiralOrder(root):
        if root is None:
                return
        q = [root]
        f = False #flag to check even or odd level
        while q:
                s = len(q)#No of nodes in q (#of node in current level)
                if f:#even level 
                        while s>0:#while all the node of cuurent level printed
                                curr = q.pop(0)
                                print(curr.key,end=" ")
                                if curr.left:
                                        q.append(curr.left)
                                if curr.right:
                                        q.append(curr.right)
                                s-=1
                else:
                        while s>0:
                                curr = q.pop()#insert at first
                                print(curr.key,end = " ")
                                if curr.right:#insert at first 
                                        q.insert(0,curr.right)#insert right first
                                if curr.left:
                                        q.insert(0,curr.left)
                                s-=1
                f = not f #change flag
                print()


root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.left.left = Node(10)
root1.left.right = Node(10)
root1.right.left = Node(30)

SpiralOrder(root1)
