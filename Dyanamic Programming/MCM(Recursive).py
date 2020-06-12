import sys
arr = [5,30,40,2]

def MCM(arr,i,j):
        if i>=j:
                return 0
        mn = sys.maxsize
        for k in range(i,j):
                temp = MCM(arr,i,k)+MCM(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
                if temp<mn:
                        mn=temp
        return mn


print(MCM(arr,1,len(arr)-1))
