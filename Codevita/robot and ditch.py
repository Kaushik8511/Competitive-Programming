#input F,B,t,FD,BD
import math

def cal_dist(f,b,fd,bd):
    if fd<=f:return fd,"F"
    if bd<=(b-f):return f+f+bd,"B"
    if f==b:return float('inf'),None

    dist_per_step = f+b
    actual_dist = abs(f-b)
    if f>b:
        steps = math.ceil((fd-f)/actual_dist)
        rem = fd - steps*actual_dist
        total = steps*dist_per_step+rem
        return total,"F"
    total = f
    bd = bd+f
    steps = math.ceil((bd-b)/actual_dist)
    rem = bd-steps*actual_dist
    total+=(steps*dist_per_step+rem)
    return total,"B"
        


def solve(f,b,t,fd,bd):
    dist,dire = cal_dist(f,b,fd,bd)
    if dire==None:
        print("No ditch")
        return
    time = dist*t
    print(f"{time} {dire}")
    
    



f,b,t,fd,bd = map(int,input().split())
solve(f,b,t,fd,bd)
