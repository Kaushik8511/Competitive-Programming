#you are given range height and width calculate how many square cadebory you can make

#to further optimize it use dynamic programming
def cal_square(a,b):
    min_s = min(a,b)
    if min_s==0:return 0
    max_s = max(a,b)
    return max_s//min_s+cal_square(max_s%min_s,min_s)


def solve(h1,h2,w1,w2):
    res = 0
    for i in range(h1,h2+1):
        for j in range(w1,w2+1):
            res+=(cal_square(i,j))
    return res


h1,h2,w1,w2 = map(int,input().split())
print(solve(h1,h2,w1,w2))
