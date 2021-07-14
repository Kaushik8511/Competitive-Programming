amt = float(input())
y = int(input())
n1 = int(input())
A=B=0
for i in range(n1):
    y1,rate = input().split()
    y1 = int(y1)
    rate = float(rate)
    emi = (amt*rate)/(1-1/((1+rate)**(12*y1)))
    A+=emi
n1 = int(input())
for i in range(n1):
    y1,rate = input().split()
    y1 = int(y1)
    rate = float(rate)
    emi = (amt*rate)/(1-1/((1+rate)**(12*y1)))
    B+=emi

if A<=B:print("Bank A")
else:print("Bank B")
