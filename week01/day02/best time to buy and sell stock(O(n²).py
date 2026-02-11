def MaxProfit (prices):
    min_price=float('inf')
    max_profit=0
    for i in range(len(prices)):
        if prices[i]<min_price:
            min_price=prices[i]
        for j in range(i+1,len(prices)):
            profit=prices[j]-min_price
            if profit>max_profit:
                max_profit=profit
    return max_profit

print(MaxProfit([7,1,5,3,6,4]))

