arr = [1,2,3,4,5,6,8,7,4,3,2,1]
ele=7

def peak(arr):
        n = len(arr)
        if (n==1 or arr[0]>arr[1]):
                return arr[0]
        if arr[n-1]>arr[n-2]:
                return arr[n-1]
        start = 1
        end = n-2
        while(start<=end):
                mid = start+(end-start)//2
                if arr[mid]>arr[mid-1]and arr[mid]>arr[mid+1]:
                        return mid
                elif arr[mid-1]>arr[mid]:
                        end = mid-1
                else:
                        start = mid+1

def BinarySearch(arr,ele,asc=True):
        start = 0
        end = len(arr)-1

        while(start<=end):
                mid = start+(end-start)//2
                if arr[mid]==ele:
                        return mid
                elif arr[mid]>ele:
                        if asc:
                                end = mid-1
                        else:
                                start = mid+1
                else:
                        if asc:
                                start = mid+1
                        else:
                                end = mid-1
        return -1

i = peak(arr)
res1 = BinarySearch(arr[:i],ele)
if res1 != -1:
        print(res1)
else:
        res2 = BinarySearch(arr[i:],ele,False)
        if res2 != -1:
                print(res2+i)
        else:
                print(res2)
