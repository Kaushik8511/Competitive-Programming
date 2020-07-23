arr = [3,3,5,3,5,2,6,7,5,4,3]

def NSR(arr):
        stack = []
        ans = []

        for i in range(len(arr)-1,-1,-1):
                if len(stack)==0:
                        ans.append(-1)
                elif stack[-1][0]>arr[i]:
                        ans.append(stack[-1][1])
                else:
                        while len(stack)!=0 and stack[-1][0]<=arr[i]:
                                stack.pop()
                        if len(stack)==0:
                                ans.append(-1)
                        else:
                                ans.append(stack[-1][1])
                stack.append([arr[i],i])
        ans.reverse()
        return ans

print(NSR(arr))
