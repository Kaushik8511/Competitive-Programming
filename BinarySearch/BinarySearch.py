arr = [1,2,3,4,5,6,7,8,9,10]
ele = 8

def binarySearch(arr,ele):
        start = 0
        end = len(arr)-1

        while(start<=end):
                mid = start+(end-start)//2
                if arr[mid]==ele:
                        return mid
                elif arr[mid]>ele:
                        end = mid-1
                else:
                        start=mid+1
        return -1

print(binarySearch(arr,ele))
                        
