class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right
def findLCA(root,lca,x,y):
        if root is None:
                return False,lca
        if root.key==x or root.key==y:
                return True,root.key
        left,lca=findLCA(root.left,lca,x,y)
        right,lca=findLCA(root.right,lca,x,y)

        if left and right:
                lca = root.key

        return (left or right),lca
        


def LCA(root,x,y):
        lca = None
        temp,lca = findLCA(root,lca,x,y)
        print(lca)

root1 = Node(9)
root1.left = Node(8)
root1.right = Node(19)
root1.left.left = Node(5)
root1.left.right = Node(6)
root1.right.left = Node(3)
root1.right.right=Node(2)


LCA(root1,2,3)
