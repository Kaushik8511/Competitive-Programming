class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key = key
                self.left = left
                self.right=right

def isComplete(root):
        if root is None:
                return
        q = [root]
        flag = False #if any node found which has no left or right child
        #then further nodes also should not have child
        #flag indicates that from this node further there is no child of any node

        while q:
                curr = q.pop(0)
                if flag and (curr.left or curr.right):
                        return False
                if not curr.left and curr.right:
                        return False
                if curr.left:
                        q.append(curr.left)
                else:
                        flag = True
                if curr.right:
                        q.append(curr.right)
                else:
                        flag = True
        return True


root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.left.left = Node(30)
root1.left.right = Node(10)
root1.right.left = Node(10)

print(isComplete(root1))
