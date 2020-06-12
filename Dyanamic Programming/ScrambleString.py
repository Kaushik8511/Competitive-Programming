X = "kaushik"
Y = "kanishe"

def scramble(X,Y):
        if X==Y:
                return True
        if len(X)<=1:
                return False
        n=len(X)
        for i in range(1,len(X)):
                ans1 = scramble(X[0:i],Y[n-i:]) and scramble(X[i:],Y[0:n-i])
                ans2 = scramble(X[0:i],Y[0:i]) and scramble(X[i:],Y[i:])
                if ans1 or ans2:
                        return True
        return False

print(scramble(X,Y))
