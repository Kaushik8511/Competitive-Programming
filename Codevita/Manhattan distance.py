def d(x,y,a,b):
    return abs(x-a)+abs(y-b)

def man_dist(iland,a,b):
    x1,y1,x2,y2 = iland['x1'],iland['y1'],iland['x2'],iland['y2']
    x3,y3 = (x1+x2+y1-y2)//2,(x2-x1+y1+y2)//2
    x4,y4 = (x1+x2+y1-y3)//2,(x1-x2+y1+y2)//2
    return min(d(x1,y1,a,b),d(x2,y2,a,b),d(x3,y3,a,b),d(x4,y4,a,b)),iland['index']


def solve(ilands,a,b):
    ilands.sort(key = lambda ilnd:man_dist(ilnd,a,b))
    for i in ilands:print(i['index'])


n = int(input())
ilands = []
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    dt = {'x1':x1,'x2':x2,'y1':y1,'y2':y2,'index':i+1}
    ilands.append(dt)
a,b = map(int,input().split())
solve(ilands,a,b)
