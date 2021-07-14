def fill(n,mat):
    count = 1
    row = col = n
    i=j=0
    checkP = 1
    res = [(0,0)]
    while i<row and j<col:
        for k in range(j,col):
            mat[i][k]=count
            if count%11==0:
                checkP+=1
                res.append((i,k))
            count+=1
        i+=1
        for k in range(i,row):
            mat[k][col-1]=count
            if count%11==0:
                checkP+=1
                res.append((k,col-1))
            count+=1
        col-=1
        if i<row:
            for k in range(col-1,j-1,-1):
                mat[row-1][k]=count
                if count%11==0:
                    checkP+=1
                    res.append((row-1,k))
                count+=1
            row-=1
        if j<col:
            for k in range(row-1,i-1,-1):
                mat[k][j]=count
                if count%11==0:
                    checkP+=1
                    res.append((k,j))
                count+=1
            j+=1
    return checkP,res
    

def solve(n):
    mat = [[None for _ in range(n)]for _ in range(n)]
    checkPoints,res = fill(n,mat)
    for i in range(n):
        for j in range(n):print(mat[i][j],end=" ")
        print()
    print("Total Power points :",checkPoints)
    for i in res:print(i)   


n = int(input())
solve(n)
