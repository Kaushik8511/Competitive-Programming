#check whether any substring of Y is angram of x or not.

def isAngram(x,y):
    m,n = len(x),len(y)
    if m>n:return False
    x_h = [0 for _ in range(26)]
    y_h = [0 for _ in range(26)]
    for i in range(m):
        x_h[ord(x[i])-ord('a')]+=1
        y_h[ord(y[i])-ord('a')]+=1
    if x_h==y_h:return True
    for i in range(1,n-m+1):
        y_h[ord(y[i-1])-ord('a')]-=1
        y_h[ord(y[i+m-1])-ord('a')]+=1
        if y_h==x_h:return True
    return False



x = input()
y = input()
print(isAngram(x,y))
