#priority queue implemented
from heapq import heappush,heappop

#calculated number of platforms required
def platforms_required(n,train):
    platforms_required_for_train = []
    heappush(platforms_required_for_train,train[0][1])
    for tr in range(1,n):
        #minimum leaving time for train till tr index
        min_dept = heappop(platforms_required_for_train)
        #print(tr,min_dept,train[tr][0]+train[tr][1])
        if train[tr][0]>min_dept:heappush(platforms_required_for_train,train[tr][1])
        else:
            heappush(platforms_required_for_train,train[tr][1])
            heappush(platforms_required_for_train,min_dept)
    #print(platforms_required_for_train)
    return len(platforms_required_for_train)

def solve(n,train):
    train.sort()
    return platforms_required(n,train)
    


#driver code
n = int(input())
train_time = []
for i in range(n):
    u,v = map(int,input().split())
    train_time.append([u,u+v])
    #print(train_time)
print(solve(n,train_time),end="")
