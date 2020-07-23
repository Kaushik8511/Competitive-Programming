arr = [0,1,0,2,1,0,1,3,2,1,2,1]

def WTP(arr):
        maxR=[arr[-1]]
        maxL=[arr[0]]
        n =len(arr)
        for i in range(1,len(arr)):
                maxR.append(max(maxR[-1],arr[n-i-1]))
                maxL.append(max(arr[i],maxL[-1]))
        water = []
        maxR.reverse()
        for i in range(len(arr)):
                water.append(min(maxR[i],maxL[i])-arr[i])
        return sum(water)

print(WTP(arr))
