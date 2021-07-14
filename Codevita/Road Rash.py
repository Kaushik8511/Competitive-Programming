import collections,math
def time(n,cars):
    t = collections.defaultdict(lambda:0)
    for x,y,v in cars:
        d = math.sqrt((x*x)+(y*y))
        t[d/v]+=1
    print(t)
    return t

def c(n):
    if n<2:return 0
    res=1
    for i in range(3,n+1):
        res*=i
    return res

n = int(input())
cars = []
for i in range(n):
    x,y,v = map(int,input().split())
    cars.append((x,y,v))
t = time(n,cars)
res = 0
for i in t:
    res+=(c(t[i]))
print(res)
