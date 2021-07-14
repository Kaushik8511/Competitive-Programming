#Here we are not considering that number itself and 1
def fact(n):
    if n<2:return []
    res = []
    i = 2
    while i*i<=n:
        if n%i==0:
            res.append(i)
            if i!=n//i:res.append(n//i)
        i+=1
    return res

print(fact(585324))
        
