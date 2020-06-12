from sys import maxsize
egg = 2
floor = 6

def eggDrop(e,f):
        if e==1 or f==1 or f==0:
                return f
        mn = maxsize
        for k in range(1,f+1):
                temp = 1+max(eggDrop(e-1,k-1),eggDrop(e,f-k))
                if mn>temp:
                        mn=temp
        return mn
print(eggDrop(egg,floor))
