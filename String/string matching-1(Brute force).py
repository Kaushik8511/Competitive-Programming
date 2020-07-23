#return if s is substring of t or not

s = "abfded"
t = "fefuafidajigffjakiogteiajndangfoitjwehngsdndsuhrouabfdenjfauhfuweyhujafsdnfabfded"

def match(s,t):
    m,n = len(t),len(s)
    if len(s)>len(t):return False

    for i in range(m-n+1):
        if s==t[i:i+n]:return True

    return False

print(match(s,t))
