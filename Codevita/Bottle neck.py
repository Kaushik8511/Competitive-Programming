import collections
def solve(bottles):
    d = collections.defaultdict(lambda:0)
    res = 0
    for i in bottles:
        d[i]+=1
        res = max(res,d[i])
    return res

bottles = list(map(int,input().split()))
print(solve(bottles))
