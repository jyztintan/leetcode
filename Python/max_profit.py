def max_profit(prices):
    if len(prices) < 2:
        return 0
    curr_lowest = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < curr_lowest:
            curr_lowest = price
        else:
            diff = price - curr_lowest
            if max_profit < diff:
                max_profit = diff
    return max_profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))
prices = [7,6,4,3,1]
print(max_profit(prices))
