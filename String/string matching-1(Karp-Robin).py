#return if s is substring of t or not

s = "wehngsdndsuhrouabfden"
t = "fefuafidajigffjakiogteiajndangfoitjwehngsdndsuhrouabfdenjfauhfuweyhujafsdnfabfded"

def char(c):return ord(c)-ord('a')+1


def Karp_robin(s,t):
    m,n = len(t),len(s)
    if m<n:return False
    p = 10**9+7

    x = temp = 0
    for i in range(n):
        x = (x*26+char(s[i]))%p
        temp = (temp*26+char(t[i]))%p
    print(x)
    if x==temp:return True
    for i in range(1,m-n+1):
        max_pow = pow(26,n,p)
        temp = (temp*26-char(t[i-1])*max_pow+char(t[i+n-1]))%p
        if x==temp:
            print(s)
            print(t[i:i+n])
            return True

    return False
        
print(Karp_robin(s,t)) 
    
