price = [100,80,60,70,60,75,85,123]

def SSP(price):
        stack = []
        days = []

        for i in range(len(price)):
                if len(stack)==0:
                        days.append(-1)
                elif stack[-1][0]>price[i]:
                        days.append(stack[-1][1])
                else:
                        while len(stack)!=0 and stack[-1][0]<=price[i]:
                                stack.pop()
                        if len(stack)==0:
                                days.append(-1)
                        else:
                                days.append(stack[-1][1])
                stack.append([price[i],i])
        print(days)
        for i in range(len(price)):
                days[i]=i-days[i]
        return days
print(SSP(price))
