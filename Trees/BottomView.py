class Node:
        def __init__(self,key=None,left=None,right=None):
                self.key=key
                self.left=left
                self.right=right
def printBottom(root,dist,level,d):
        if root is None:
                return
        if dist not in d or level>=d[dist][1]:
                d[dist]=[root.key,level]
        printBottom(root.left,dist-1,level+1,d)
        printBottom(root.right,dist+1,level+1,d)

def bottomView(root):
        d = {}
        printBottom(root,0,0,d)
        for dist in sorted(d.keys()):
                print(d[dist][0],end=" ")


root1 = Node(20)
root1.left = Node(30)
root1.right = Node(20)
root1.right.left = Node(30)
root1.right.left.left = Node(10)
root1.left.right = Node(10)

bottomView(root1)
