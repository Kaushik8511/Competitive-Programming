num = int(input("enter a number"))

def isPrime(n):
        if n==0 or n==1:
                return False
        for i in range(2,n//2+1):
                if n%i==0:
                        return False
        return True

if isPrime(num):
        print("prime number")
else:
        print("Non prime number")
