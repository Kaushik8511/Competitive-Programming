import sys
arr = [5,30,40,2]
t = [[-1 for i in range(len(arr))]for j in range(len(arr))]

def MCM(arr,i,j):
        if (i>=j):
                t[i][j]=0
                return 0
        if t[i][j] != -1:
                return t[i][j]
        mn = sys.maxsize
        for k in range(i,j):
                temp = MCM(arr,i,k)+MCM(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
                if temp<mn:
                        mn=temp
        t[i][j]=mn
        return t[i][j]

print(MCM(arr,1,len(arr)-1))
for i in t:
        print(i)
