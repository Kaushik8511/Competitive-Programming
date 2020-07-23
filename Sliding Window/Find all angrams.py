x = "ababcbabcbabcbjbbsbabjfbabac"
y = "abc"

def fun(x,y):
    if len(y)>len(x):return []

    h1 = [0 for i in range(26)]
    h2 = [0 for i in range(26)]

    for i in range(len(y)):
        h1[ord(y[i])-ord('a')]+=1
        h2[ord(x[i])-ord('a')]+=1
    res = []
    if h1==h2:res.append(0)

    for i in range(1,len(x)-len(y)+1):
        h2[ord(x[i-1])-ord('a')]-=1
        h2[ord(x[i+len(y)-1])-ord('a')]+=1
        if h1==h2:res.append(i)

    return res

print(fun(x,y))
