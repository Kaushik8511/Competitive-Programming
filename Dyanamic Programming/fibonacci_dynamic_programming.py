n = int(input("enter which term you want to know : "))
fib = [0,1]
for i in range(2,n):
	fib.append(fib[i-1]+fib[i-2])
print(fib[n-1])