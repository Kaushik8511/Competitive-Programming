from math import sqrt,sin,cos,asin,radians

#calculationg how long signal can reached based on height
def how_long(h):
    res=round(2*h*6371,6)
    ret=round(sqrt(res),6)
    return ret

#calculating distance based on lattitude and longitude
def har_dist(lt1,lt2,ln1,ln2):
    lt1,ln1,lt2,ln2 = radians(lt1),radians(ln1),radians(lt2),radians(ln2)
    difflt = lt2 - lt1
    diffln = ln2 - ln1
    temp = round((sin(difflt/2)**2 + cos(lt1) * cos(lt2) * sin(diffln/2)** 2),6)
    d = round(2 * asin(sqrt(temp)),6)
    return round(d * 6371)

#function to compare two distances
def can_reached(lt,ln,h,loc):
    #max distance
    dist_1=round(how_long(h),6)
    dist_2=har_dist(lt,loc[0],ln,loc[1])
    #print(dist_1,dist_2)
    return dist_2<=dist_1

#driver function
def solve(n,latitudes,longitudes,heights,location):
    reached = 0
    for i in range(n):
        if can_reached(latitudes[i],longitudes[i],heights[i],location):reached+=1
    print(reached)

#taking inputs
try:
    flag = True
    n = int(input())
    latitudes = list(map(float,input().split()))
    longitudes = list(map(float,input().split()))
    heights = list(map(int,input().split()))
    location = list(map(float,input().split()))
except:
    flag = False
    print()
if flag:solve(n,latitudes,longitudes,heights,location)
