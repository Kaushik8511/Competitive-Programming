def solve(s):
    error = "Compilation Errors"
    noError = "No Compilation Errors"

    if len(s)<2:return error
    if s[0]!='{' or s[-1]!='}':return error
    main = 0
    ismain = False
    isfun = False
    st = []
    stm = 0
    # {, }, (, ), <, >
    for i in range(len(s)):
        if s[i]==" ":continue
        #print(s[i],st)
        if s[i]=='P':
            stm+=1
            if isfun and not ismain and stm>100:
                #print(stm,isfun) 
                return error
            continue
        elif s[i]=='{':
            if i!=0 and not isfun:return error
            st.append(s[i])
        elif s[i]=='}':
            if not st or st[-1]!='{':return error
            st.pop()
        elif s[i]=='(':
            if isfun:return error
            isfun=True
            st.append(s[i])
            stm = 0
        elif s[i]==')':
            if not st or st[-1]!='(':return error
            st.pop()
            isfun=False
        elif s[i]=='<':
            if isfun:return error
            main+=1
            isfun=True
            ismain=True
            st.append(s[i])
            stm = 0
        else:
            if not st or st[-1]!='<':return error
            isfun=False
            ismain=False
            st.pop()
    if main!=1:return error
    if st:return error
    return noError      
        

s = input()
print(solve(s))
