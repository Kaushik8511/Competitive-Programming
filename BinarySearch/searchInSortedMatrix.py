mat = [[10,20,30,40],
       [15,25,35,45],
       [27,29,37,45],
       [32,33,39,50]]
ele = 22
def SortMatrix(mat,ele):
        row = 0
        col = len(mat[0])-1

        while(row<len(mat) and col>=0):
                if mat[row][col]==ele:
                        return row,col
                elif mat[row][col]>ele:
                        col-=1
                else:
                        row+=1
        return -1
print(SortMatrix(mat,ele))
