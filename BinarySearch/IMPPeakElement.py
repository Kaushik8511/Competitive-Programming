arr = [2,2,1,1,2,6,5,4,3]

def peakElement(arr):
        n = len(arr)
        if n==1 or arr[0]>arr[1]:
                return arr[0]
        if arr[n-2]<arr[n-1]:
                return arr[n-1]

        start = 1
        end = n-2

        while(start<=end):
                mid = start+(end-start)//2
                if (arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
                        return arr[mid]
                elif arr[mid]<arr[mid-1]:
                        end = mid-1
                else:
                        start = mid+1

print(peakElement(arr))
                        
