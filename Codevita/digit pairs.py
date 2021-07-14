def cal_bitscore(a,b):
    score = str(int(a)*11+int(b)*7)
    if len(score)>2:return score[-2:]
    return score

def cal_pair(n):
    if n<2:return 0
    if n==2:return 1
    return 2


def solve(nums):
    bitscore = []
    for num in nums:
        mx,mn = max(num),min(num)
        bitscore.append(cal_bitscore(mx,mn))
    odd = [0 for _ in range(10)]
    even = [0 for _ in range(10)]
    for i in range(len(bitscore)):
        if i&1:
            even[int(bitscore[i][0])]+=1
        else:
            odd[int(bitscore[i][0])]+=1
    res = 0
    for i in range(10):
        temp = cal_pair(even[i])+cal_pair(odd[i])
        res+=min(temp,2)
    return res


nums  = list(input().split())
print(solve(nums))
