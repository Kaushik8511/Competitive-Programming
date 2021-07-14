def solve(s):
    st = []
    res = 0
    bal = True

    o = ['{','(','[']
    c = ['}',')',']']
    
    for i in range(len(s)):
        if s[i] in o:
            st.append([s[i],0])
        elif s[i]=='*':
            if len(st)!=0:st[-1][1]+=1
        elif s[i] in c:
            if len(st)==0:
                bal=False
                continue
            ind = c.index(s[i])
            br,stars = st.pop()
            if br!=o[ind]:
                if len(st)==0:continue
                st[-1][1]+=stars
                bal = False
            else:
                if stars>1:res+=1
                else:bal=False
                if len(st)==0:continue
                st[-1][1]+=stars
    if bal:print("yes",end=" ")
    else:print("No",end=" ")
    print(res)


            
            

    

s = input()
solve(s)
