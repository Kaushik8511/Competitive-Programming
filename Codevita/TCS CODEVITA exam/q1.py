no_of_gifts = [0]*(10**5+1)

#when ele is less than both left and right
def lesser_than_both(n,ranks_of_emp,no_of_gifts):
    for i in range(1,n+1):
        if ranks_of_emp[i-1] >= ranks_of_emp[i] <= ranks_of_emp[i+1]:
            no_of_gifts[i] = 1
#when ele is less than right and greater than left
def lesser_than_right(n,ranks_of_emp,no_of_gifts):
    for i in range(1,n+1):
        if ranks_of_emp[i-1] < ranks_of_emp[i] <= ranks_of_emp[i+1]:
            no_of_gifts[i] = no_of_gifts[i-1] + 1
#when ele is less than left and greater than right
def greater_than_right(n,ranks_of_emp,no_of_gifts):
    for i in range(n,0,-1):
        if ranks_of_emp[i-1] >= ranks_of_emp[i] > ranks_of_emp[i+1]:
            no_of_gifts[i] = no_of_gifts[i+1] + 1
#when ele is greater than both left and right
def greater_than_both(n,ranks_of_emp,no_of_gifts):
    for i in range(1,n+1):
        if ranks_of_emp[i-1] < ranks_of_emp[i] > ranks_of_emp[i+1]:
            no_of_gifts[i] = max(no_of_gifts[i-1], no_of_gifts[i+1]) + 1
            
def solve(n,ranks_of_emp):
    #to handle edge cases we inserted max value at left and right side
    ranks_of_emp.insert(0,10**9+19)
    ranks_of_emp.append(10**9+19)
    #print(ranks_of_emp)
    lesser_than_both(n, ranks_of_emp, no_of_gifts)
    lesser_than_right(n, ranks_of_emp, no_of_gifts)
    greater_than_right(n, ranks_of_emp, no_of_gifts)
    greater_than_both(n, ranks_of_emp, no_of_gifts)
    #print(no_of_gifts)
    print (sum(no_of_gifts),end="")

#driver code
t = int(input())
while t:
    n = int(input())
    ranks_of_emp = list(map(int,input().split()))
    solve(n,ranks_of_emp)
    if t!=1:print()
    t-=1
