def convert(s,b):
    l = len(s)-1
    res = 0
    for i in s:
        if i.isdigit():temp=int(i)
        else:temp=ord(i)-ord('A')+10
        res+=((b**l)*temp)
        l-=1
    return res

print(convert("123ABCDEF",16))
