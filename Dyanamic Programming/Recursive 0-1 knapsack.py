wt = [2,3,4,5]
val = [6,10,5,7]
W = 7

def recursiveKnapsack(wt,val,W,n):
	if n==0 or W==0:
		return 0
	elif wt[n-1]<=W:
		return max(recursiveKnapsack(wt,val,W-wt[n-1],n-1)+val[n-1],recursiveKnapsack(wt,val,W,n-1))
	elif wt[n-1]>W:
		return recursiveKnapsack(wt,val,W,n-1)

print(recursiveKnapsack(wt,val,W,len(wt)))
