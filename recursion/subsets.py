A = [13,12]

def subsets(A,pos,res,fr):
        if pos==len(A):
                fr.append(res.copy())
                return

        subsets(A,pos+1,res.copy(),fr)
        res.append(A[pos])
        subsets(A,pos+1,res.copy(),fr)

def sub(A):
        fr = []
        subsets(A,0,[],fr)
        print(fr)

sub(A)
