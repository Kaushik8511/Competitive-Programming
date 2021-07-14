def funn(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    i=0
    res=""
    while num:
        res+=(numerals[i] * (num//values[i]))
        num=num%values[i]
        i+=1
    return res
def base(b):
    return ord(b)-ord('A')+11

def convert(s,b):
    l = len(s)-1
    res = 0
    for i in s:
        if i.isdigit():temp=int(i)
        else:temp=ord(i)-ord('A')+10
        res+=((b**l)*temp)
        l-=1
    return res


n = int(input())
while 1<=n<4000:
    x = funn(n)
    mn = base(max(x))
    n = convert(x,mn)
    print(x,mn,n)
print(n)
