def solve(s,temp):
    d = {}
    for i in range(len(temp)):
        d[temp[i]]=i
    res = 0
    #prev_ind = None
    prev_char = None
    flag = False
    for i in range(len(s)):
        if s[i] in d:
            #print(i,prev_char)
            if prev_char!=None and d[s[i]]==d[prev_char[-1]]+1:
                if flag:
                    res+=1
                    prev_char = s[i]
                    #prev_ind = i
                    flag = False
                    continue
                prev_char += s[i]
                #prev_ind = i
                continue
            if prev_char!=None and s[i]==prev_char[-1]:
                if prev_char.count(s[i])!=len(prev_char):
                    res+=1
                    prev_char = s[i]
                    continue
                flag = True
                prev_char += s[i]
                #prev_ind = i
                continue
            prev_char = s[i]
            #prev_ind = i
            #print(i,s[i])
            res+=1
    return res


s = input()
temp = input()
print(solve(s,temp))
