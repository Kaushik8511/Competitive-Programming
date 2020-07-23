a = [1,2,1]


def permutations(A,left,right,res):
        if left==right:
                res.append(A.copy())
                
        else:
                for i in range(left,right+1):
                        A[i],A[left] = A[left],A[i]
                        
                        permutations(A,left+1,right,res)
                        A[i],A[left] = A[left],A[i]
def per(A):
        if len(A)==0:
                return []
        res = []
        permutations(A,0,len(A)-1,res)
        return res


print(per(a))
