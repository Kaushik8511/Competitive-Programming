expr = "T&F&T|F^T"

def ExprEval(expr,i,j,istrue):
        if i>j:
                return False
        if i==j:
                if istrue:
                        return expr[i]=='T'
                else:
                        return expr[i]=='F'
        ans=0
        for k in range(i+1,j,2):
                lt = ExprEval(expr,i,k-1,True)
                lf = ExprEval(expr,i,k-1,False)
                rt = ExprEval(expr,k+1,j,True)
                rf = ExprEval(expr,k+1,j,False)

                if expr[k]=='&':
                        if istrue:
                                ans+=lt*rt
                        else:
                                ans+=lf*rt+lt*rf+lf*rf
                elif expr[k]=="|":
                        if istrue:
                                ans+=lt*rt+lt*rf+lf*rt
                        else:
                                ans+=lf*rf
                elif expr[k]=="^":
                        if istrue:
                                ans+=lf*rt+lt*rf
                        else:
                                ans+=lt*rt+lf*rf
        return ans

print(ExprEval(expr,0,len(expr)-1,True))
