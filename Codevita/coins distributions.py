def solve(n):
    res = [1,2,2,3,3,4,4,5,4]
    if n<10:return res[n-1]
    coin_of_5 = (n-5)//5
    rem = n-coin_of_5*5
    total = coin_of_5+res[rem-1]
    return total


n = int(input())
print(solve(n))
