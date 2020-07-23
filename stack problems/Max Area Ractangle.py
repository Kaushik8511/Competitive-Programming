arr = [[0,1,1,0],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,0,0]]

def NS(arr,left=True):
        stack = []
        ans = []
        if left:
                x = 0
                y = len(arr)
                z = 1
                default = -1
        else:
                x = len(arr)-1
                y = -1
                z = -1
                default = len(arr)
        for i in range(x,y,z):
                if len(stack)==0:
                        ans.append(default)
                elif stack[-1][0]<arr[i]:
                        ans.append(stack[-1][1])
                else:
                        while len(stack)!=0 and stack[-1][0]>=arr[i]:
                                stack.pop()
                        if len(stack)==0:
                                ans.append(default)
                        else:
                                ans.append(stack[-1][1])
                stack.append([arr[i],i])
        if not left:
                ans.reverse()
        return ans

def MAH(arr):
        nsl = NS(arr)
        nsr = NS(arr,False)
        area = []
        width = []
        for i in range(len(arr)):
                width.append(nsr[i]-nsl[i]-1)
                area.append(width[i]*arr[i])
        return max(area)

def MAR(arr):
        ar = arr[0]
        area = MAH(ar)
        for i in range(1,len(arr)):
                for j in range(len(arr[0])):
                        if arr[i][j]==0:
                                ar[j]=0
                        else:
                                ar[j]+=1
                area = max(area,MAH(ar))
        return area
                        
print(MAR(arr))
