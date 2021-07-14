def funn(s):
    di = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    i=0
    res=0
    while i<len(s):
        if i+1<len(s) and di[s[i+1]]>di[s[i]]:
            res+=(di[s[i+1]]-di[s[i]])
            i+=1
        else:res+=di[s[i]]
        i+=1
            

    return res


print(funn("DCCXXIX"))
