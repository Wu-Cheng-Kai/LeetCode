prices = [7,6,4,3,1]

# # 1. double for loop >> time out(198)
# max_profit = 0

# for buy in range(len(prices)-1):
#     for sell in range(buy+1, len(prices)):
#         profit = prices[sell] - prices[buy]
#         if profit > max_profit:
#             max_profit = profit

# # 2. for loop  + max >> time out(200)
# max_profit = 0

# for buy in range(len(prices)-1):
#     profit = max(prices[buy+1:]) - prices[buy]
#     if profit > max_profit:
#         max_profit = profit

# 3. dynamic programming
max_profit, profit = 0, 0

for i in range(1, len(prices)):
    profit += prices[i] - prices[i-1]
    if profit > 0:
        if profit > max_profit:
            max_profit = profit
    else:
        profit = 0

print(max_profit)