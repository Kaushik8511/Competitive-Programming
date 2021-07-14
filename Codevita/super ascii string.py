def solve(s):
    if len(s)==0:return True
    h = [0 for _ in range(26)]
    for c in s:
        ind = ord(c)-ord('a')
        h[ind]+=1
    for i in range(26):
        if h[i]!=0 and h[i]!=(i+1):return False
    return True


s = input()
if solve(s):print("yes")
else:print("No")
