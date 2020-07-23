a = [0,5,1,2]

def insert(A,temp):
        if len(A)==0 or A[-1]<=temp:
                A.append(temp)
                return
        val = A.pop()
        insert(A,temp)
        A.append(val)

def sort(A):
        if len(A)<=1:
                return
        temp = A.pop()
        sort(A)
        insert(A,temp)

sort(a)
print(a)
