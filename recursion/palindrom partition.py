s = "palindrom"

def ispalindrom(s,i,j):
        while i<j:
                if s[i]!=s[j]:
                        return False
        return True

def partition(s,i,j,res):
        if i>=j:
                res.append(s[i])
                return
        if ispalindrom(s,i,j):
                res.append(s[i:j+1])
                return
        for k in range(i,j):
                partition(s,i,k,res)
                partition(s,k+1,j,res)

res = []
partition(s,0,len(s)-1,res)
print(res)
        
