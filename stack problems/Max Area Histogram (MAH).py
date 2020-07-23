arr = [6,2,5,4,5,1,6]

def NS(arr,left=True):
        stack = []
        ans = []
        if left:
                x=0
                y=len(arr)
                z=1
                default = -1
        else:
                x=len(arr)-1
                y=-1
                z=-1
                default = len(arr)
        for i in range(x,y,z):
                if (len(stack)==0):
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
        print(nsl)
        print(nsr)
        width=[]
        area = []
        for i in range(len(arr)):
                width.append(nsr[i]-nsl[i]-1)
                area.append(width[i]*arr[i])
        print(area)
        return max(area)

print(MAH(arr))
