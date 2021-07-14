def find_angle(hr,mins):
    hr = (hr*5)+(mins/12)
    angle = abs(hr-mins)*6
    return min(angle,360-angle)


def solve(hrs,long):
    diff = (hrs*long)/360
    diff *= 60
    hr = (diff//60)%12
    mins = diff%60
    angle = find_angle(hr,mins)
    print(angle)

hr_in_day = int(input())
long = float(input())
solve(hr_in_day,long)
