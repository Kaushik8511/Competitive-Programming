from sys import maxsize
egg = 2
floor = 6
t = [[-1 for i in range(floor+1)]for j in range(egg+1)]

def MEMEgg(e,f):
        if e==1 or f==0 or f==1:
                return f
        mn = maxsize
        if t[e][f]!=-1:
                return t[e][f]
        for k in range(1,f+1):
                temp = 1+max(MEMEgg(e-1,k-1),MEMEgg(e,f-k))
                if temp<mn:
                        mn = temp
        t[e][f]=mn
        return t[e][f]

print(MEMEgg(egg,floor))
for i in t:
        print(i)
