arr = [1,2,3,4,5,5,5,5,5,6,7]
ele = 5

def countEle(arr,ele,first=True):
        start = 0
        end = len(arr)-1
        res = -1

        while(start<=end):
                mid = start+(end-start)//2
                if arr[mid]==ele:
                        res = mid
                        if first:
                                end = mid-1
                        else:
                                start = mid+1
                elif arr[mid]>ele:
                        end = mid-1
                else:
                        start = mid+1
        return res

last = countEle(arr,ele,False)
first = countEle(arr,ele)
ans = last-first+1
if ans==-1:
        ans = 0
print(ans)
