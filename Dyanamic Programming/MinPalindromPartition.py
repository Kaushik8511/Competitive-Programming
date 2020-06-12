from sys import maxsize
s = "kaushikrk"

def ispalindrom(s,i,j):
        while(i<j):
                if s[i]!=s[j]:
                        return False
                i+=1
                j-=1
        return True

def MPP(s,i,j):
        if i>=j:
                return 0
        if ispalindrom(s,i,j):
                return 0
        mn = maxsize
        for k in range(i,j):
                temp = 1+MPP(s,i,k)+MPP(s,k+1,j)
                if temp<mn:
                        mn=temp
        return mn

print(MPP(s,0,len(s)-1))
