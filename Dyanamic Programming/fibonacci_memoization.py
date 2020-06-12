def fib(n,li):
	if len(li)>=n:
		return li[n-1]
	temp=fib(n-1,li)+fib(n-2,li)
	li.append(temp)
	return li[n-1]
li=[0,1]
print(fib(100,li))