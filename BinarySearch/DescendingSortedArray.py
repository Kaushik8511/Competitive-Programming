arr = [10,9,8,7,6,5,4,3,2,1]
ele = 1

def DescBS(arr,ele):
        start = 0
        end = len(arr)-1

        while(start<=end):
                mid = start+(end-start)//2
                if arr[mid]==ele:
                        return mid
                elif arr[mid]>ele:
                        start = mid+1
                else:
                        end = mid-1
        return -1

print(DescBS(arr,ele))
