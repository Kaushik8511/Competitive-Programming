s = []
ss = []

def getMin():
        if len(ss)==0:
                return -1
        return ss[-1]

def push(a):
        if len(s)==0 or ss[-1]>=a:
                s.append(a)
                ss.append(a)
        else:
                s.append(a)
                
def pop():
        if len(s)==0:
                return -1
        if s[-1]==ss[-1]:
                ss.pop()
        s.pop()
push(4)
push(2)
print(getMin())
pop()
push(6)
push(8)
push(8)
push(54)
push(6)
push(1)
push(2)
push(4)
pop()
pop()
pop()
print(s)
print(ss)
