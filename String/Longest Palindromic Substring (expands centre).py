x = "adsffxfxcdfccccaaacacacacacacaa"

def expand(s,i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return j-i-1

def LPS(x):
    if len(x)<2:return x
    start=end=0
    for i in range(len(x)):
        l = max(expand(x,i,i),expand(x,i,i+1))
        if l>end-start:
            start = i-((l-1)//2)
            end = i+(l//2)
    return x[start:end+1]

print(LPS(x))
