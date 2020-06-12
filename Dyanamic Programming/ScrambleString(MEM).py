X = "great"
Y = "rgaet"
d = {}

def Scramble(X,Y):
        if X==Y:
                return True
        if len(X)<=1:
                return False
        key = X+" "+Y
        if key in d:
                return d[key]
        n=len(X)
        for i in range(1,len(X)):
                f1 = Scramble(X[:i],Y[n-i:])and Scramble(X[i:],Y[0:n-i])
                f2 = Scramble(X[:i],Y[:i])and Scramble(X[i:],Y[i:])
                if f1 or f2:
                        d[key]=True
                        return d[key]
        d[key]=False
        return d[key]
print(Scramble(X,Y))
for i,j in d.items():
        print(i,"   :",j)
