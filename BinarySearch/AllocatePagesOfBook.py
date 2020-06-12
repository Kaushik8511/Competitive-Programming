page = [10,45,43,23,12,70,20,30,40]
student = 4

def isvalid(page,mid,st):
        temp = 1
        sm = 0
        for i in range(len(page)):
                sm+=page[i]
                if sm>mid:
                        temp +=1
                        sm = page[i]
                if temp>st:
                        return False
        return True


def allocateBook(page,st):
        if len(page)<st:
                return -1
        start = max(page)
        end = sum(page)
        res = -1
        while(start<=end):
                mid = start+(end-start)//2
                if(isvalid(page,mid,st)):
                        res = mid
                        end = mid-1
                else:
                        start = mid+1
        return res

print(allocateBook(page,student))
