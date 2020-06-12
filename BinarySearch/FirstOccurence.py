arr = [1,2,3,4,5,5,5,5,5,6,7]
ele = 8

def FirstOccurence(arr,ele):
        start = 0
        end = len(arr)-1
        res = -1

        while(start<=end):
                mid = start+(end-start)//2
                if arr[mid]==ele:
                        res=mid
                        end = mid-1
                elif arr[mid]>ele:
                        end = mid-1
                else:
                        start = mid+1
        return res
print(FirstOccurence(arr,ele))
