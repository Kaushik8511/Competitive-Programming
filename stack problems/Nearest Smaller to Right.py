arr = [5,4,3,6,3,6,3,2,5,4]

def NSR(arr):
        stack = []
        ans = []

        for i in range(len(arr)-1,-1,-1):
                if len(stack)==0:
                        ans.append(-1)
                elif stack[-1]<arr[i]:
                        ans.append(stack[-1])
                else:
                        while len(stack)!=0 and stack[-1]>=arr[i]:
                                stack.pop()
                        if len(stack)==0:
                                ans.append(-1)
                        else:
                                ans.append(stack[-1])
                stack.append(arr[i])
        ans.reverse()
        return ans

print(NSR(arr))
