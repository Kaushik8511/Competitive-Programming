arr = [2,3,4,5,7,8,10,21]
ele = 15

def MinDistance(arr,ele):
        start = 0
        end = len(arr)-1

        while(start<=end):
                mid = start+(end-start)//2
                if arr[mid]==ele:
                        return ele
                elif arr[mid]>ele:
                        end = mid-1
                else:
                        start = mid+1
        if (end>=0):
                res1 = ele-arr[end]
        else:
                return arr[start]
        if (start<len(arr)):
                res2 = arr[start]-ele
        else:
                return arr[end]
        if res1<res2:
                return arr[end]
        return arr[start]

print(MinDistance(arr,ele))
