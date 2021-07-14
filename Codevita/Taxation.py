def solve(tax,amt,rate,mx,rebate):
    res = amt[0]
    for i in range(len(rate)-1):
        if tax>=mx[i]:
            res+=(amt[i+1]-amt[i])
            tax-=mx[i]
            continue
        temp = (100*tax)//rate[i]
        res+=temp
        tax = 0
        break
    if tax>0:
        res+=((100*tax)//rate[-1])
    return (res+rebate)
              
    
    

n = int(input())
amt = list(map(int,input().split()))
rate = list(map(int,input().split()))
mx = [None for  _ in range(n)]
prev = 0
for i in range(n):
    mx[i] = (rate[i]*(amt[i]-prev))//100
    prev = amt[i]

emp_tax = list(map(int,input().split()))
rebate = int(input())

res = 0
temp = []
for tax in emp_tax:
    a = solve(tax,amt,rate,mx,rebate)
    res+=a
    temp.append(a)
print(temp)
print(res)
