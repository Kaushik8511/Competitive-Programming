# A or X==B find how many X's are there which satisfy the condition

a = 10
b = 11

def fun(a,b):
    count=1
    while a or b:
        if a&1:
            if b&1:count*=2
            else:return 0
        a=a>>1
        b=b>>1
    return count

print(fun(a,b))
