arr = [2,3,4,5,4,3,2,1]

def maxBiomatic(arr):
        n = len(arr)
        if (n==1 or arr[0]>arr[1]):
                return arr[0]
        if (arr[n-1]>arr[n-2]):
                return arr[n-1]
        start = 1
        end = n-2

        while(start<=end):
                mid = start+(end-start)//2
                if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                    return arr[mid]
                elif arr[mid-1]>arr[mid]:
                        end = mid-1
                else:
                        start = mid+1

print(maxBiomatic(arr))
