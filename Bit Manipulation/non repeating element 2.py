#all element repeat thrices except one element

arr = [1,1,1,2,2,2,3,3,3,1,1,1,4,4,4,8,5,4,5,4,4,5]

def fun(arr):
    one=two=0
    for i in arr:
        two|=(one & i)
        one^=i
        not_three=~(one & two)
        one&=not_three
        two&=not_three
    return one

print(fun(arr))
