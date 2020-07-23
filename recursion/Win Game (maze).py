maze = [[1,1,0],
        [1,1,0],
        [0,1,1]]


def find(maze,x,y,path):
        print(x,y)
        if x==len(maze)-1 and y==len(maze[0])-1:
                return True
        if x<0 or y<0 or x>=len(maze) or y>=len(maze[0]) or maze[x][y]==0:
                return False
        if path[x][y]==1:
                return False
        path[x][y]=1

        #right side
        if find(maze,x,y+1,path):
                path[x][y]=0
                return True
        #left
        if find(maze,x,y-1,path):
                path[x][y]=0
                return True
        #up
        if find(maze,x-1,y,path):
                path[x][y]=0
                return True
        #bottom
        if find(maze,x+1,y,path):
                path[x][y]=0
                return True

        path[x][y]=0
        return False


def findPath(maze):
        path = [[0]*len(maze[0])]*len(maze)
        print(find(maze,0,0,path))
        for i in path:
                print(i)

findPath(maze)
