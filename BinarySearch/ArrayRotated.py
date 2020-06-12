arr = [9,11,12,10,2,4,5,6,7,8,9,9,9,9]

def Rotated(arr):
        n = len(arr)
        start = 0
        end = n-1
        if arr[start]<arr[end]:
                return 0

        while(start<=end):
                mid = start+(end-start)//2
                nx = mid+1
                pre = mid-1
                if nx==n:
                        nx=0
                if pre==-1:
                        pre=n-1
                if arr[mid]<arr[pre] and arr[mid]<=arr[nx]:
                        return (n-mid),arr[mid]
                elif arr[start]<=arr[mid]:
                        start = mid+1
                elif arr[mid]<=arr[start]:
                        end = mid-1
print("Rotated, min")
print(Rotated(arr))
