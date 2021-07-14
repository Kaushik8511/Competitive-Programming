def solve(n,bottles,x):
    bottles.sort()
    for i in range(n-2):
        if i==0 or bottles[i]!=bottles[i-1]:
            sm = x-bottles[i]
            start,end = i+1,n-1
            while start<end:
                temp = bottles[start]+bottles[end]
                if temp==sm:return True
                if temp>sm:end-=1
                else:start+=1
    return False


n = int(input())
bottles = [int(input()) for _ in range(n)]
x = int(input())
print(solve(n,bottles,x))
