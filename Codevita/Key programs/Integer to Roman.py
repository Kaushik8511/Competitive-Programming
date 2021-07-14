def funn(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    i=0
    res=""
    while num:
        res+=(numerals[i] * (num//values[i]))
        num=num%values[i]
        i+=1
    return res


print(funn(575))
