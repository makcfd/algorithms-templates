def maxProfit(prices):
    i = 0
    local_min = prices[0]
    local_max = prices[0]
    profit = 0
    while i < (len(prices)-1):
        if prices[i] >= prices[i+1]:
            i += 1
            local_min = prices[i]
            local_max = prices[i]
        else:
            local_min = prices[i]
            i += 1
            local_max = prices[i]
        profit += local_max - local_min
    print(profit)


maxProfit([7,1,5,3,6,4])
