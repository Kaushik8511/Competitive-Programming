d = {}

def solve(n,opp,s):
    if len(s)==0:return 0
    if len(s)==1:return opp[0]
    if s in d:
        #print("yes")
        return d[s]
    res = 0
    for i in range(n):
        temp = opp.copy()
        prev = temp[i-1] if i>0 else 0
        nxt  = temp[i+1] if i+1<n else 0
        ss = temp.pop(i) # O(1) time by taking two variables start and end
        val = 0
        #if i==0 or i==n:val = ss
        if prev>nxt:val = prev*ss+nxt
        else:val = nxt*ss+prev
        soff = s[:i]+s[i+1:] # O(1) time by taking two variables start and end
        #print(opp[i],val)
        res = max(res,(solve(n-1,temp,soff)+val))
    d[s]=res
    return res
     



n = int(input())
opp = list(map(int,input().split()))
s = ''.join(list(map(str,opp)))
#print(s)
print(solve(n,opp,s))
