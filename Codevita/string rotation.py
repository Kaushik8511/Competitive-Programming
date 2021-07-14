import collections

def isAng(x,y):
    m,n = len(x),len(y)
    if m>n:return False
    xh = [0 for _ in range(26)]
    yh = [0 for _ in range(26)]

    for i in range(m):
        xh[ord(x[i])-ord('a')]+=1
        yh[ord(y[i])-ord('a')]+=1
    if xh==yh:return True
    for i in range(n-m+1):
        yh[ord(y[i-1])-ord('a')]-=1
        yh[ord(y[i+m-1])-ord('a')]+=1
        if xh==yh:return True
    return False

        

s = input()
first = []
n = int(input())
ind = 0
l = len(s)
for i in range(n):
    dr,m = input().split()
    m = int(m)
    if dr=="L":ind=(ind+m)%l
    else:ind=(ind-m)%l
    first.append(s[ind])
first = ''.join(first)
if isAng(first,s):print("Yes")
else:print("No")
