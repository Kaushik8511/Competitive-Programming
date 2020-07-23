num1 = 20400
num2 = 45000

def GCD(a,b):
        if b==0:
                return a
        return GCD(b,a%b)


print(GCD(num1,num2))
