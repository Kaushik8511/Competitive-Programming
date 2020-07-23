arr = [3,4,3,3,5,32,34,3,2,4]

def NSL(arr):
        stack = []
        ans = []

        for i in range(len(arr)):
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
        return ans

print(NSL(arr))
