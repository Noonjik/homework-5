#Ice Cream Parlor

def what_flavors(money, cost):
    indexes = []
    for i in range(0, len(cost)//2):
        if cost[i] and money-cost[i] in cost:
            if cost[i] != money-cost[i]:
                indexes.append(i+1)
                indexes.append(cost.index(money-cost[i])+1)
            else:
                indexes.append(i+1)
                cost.remove(cost[i])
                indexes.append(cost.index(cost[i])+2) 
        return indexes, cost[i], money-cost[i]

#inputting
t = int(input('number of trips: t= ').strip())
for t_itr in range(0,t):
    money = int(input('money =' ).strip())
    n = int(input('number of icecreams ').strip())
    cost = list(map(int, input('costs = ').rstrip().split()))
    print(what_flavors(money, cost))
