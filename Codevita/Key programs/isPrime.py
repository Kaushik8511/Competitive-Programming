def isPrime(n):
    if n<2:return False
    if n==2:return True
    if n&1==0:return False
    i=3
    while i*i<=n:
        if n%i==0:return False
        i+=2
    return True



print(isPrime(257))
