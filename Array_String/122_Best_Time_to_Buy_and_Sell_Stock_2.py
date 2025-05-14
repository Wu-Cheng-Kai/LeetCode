prices = [1,2,3,4,5]

# 1. dynamic programming
max_profit, profit = 0, 0

for i in range(1, len(prices)):
    profit = prices[i] - prices[i-1]
    if profit > 0:
        max_profit += profit

print(max_profit)
