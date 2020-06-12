expr = "T&F&T|F^T"
d = {}

def MEMExpr(expr,i,j,istrue):
        if i>j:
                return False
        if i==j:
                if istrue:
                        return expr[i]=="T"
                else:
                        return expr[i]=="F"
        key = str(i)+" "+str(j)+" "+str(istrue)
        if key in d:
                return d[key]
        ans=0
        for k in range(i+1,j,2):
                lt = MEMExpr(expr,i,k-1,True)
                lf = MEMExpr(expr,i,k-1,False)
                rt = MEMExpr(expr,k+1,j,True)
                rf = MEMExpr(expr,k+1,j,False)

                if expr[k]=="&":
                        if istrue:
                                ans+=lt*rt
                        else:
                                ans+=lf*rf+lf*rt+lt*rf
                elif expr[k]=="|":
                        if istrue:
                                ans+=lt*rt+lt*rf+lf*rt
                        else:
                                ans+=lf*rf
                elif expr[k]=="^":
                        if istrue:
                                ans+=lt*rf+rt*lf
                        else:
                                ans+=lt*rt+lf*rf
        d[key]=ans
        return d[key]

print(MEMExpr(expr,0,len(expr)-1,True))
for key,value in d.items():
        print(key," : ",value)
