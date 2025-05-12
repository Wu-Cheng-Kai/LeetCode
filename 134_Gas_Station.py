gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

check, current, total = -1, 0, 0
for i in range(len(gas)):
    save = gas[i] - cost[i]
    current += save
    total += save
    if current >= 0:
        if check < 0:
            check = i
    else:
        check = -1
        current = 0   

# return -1 if all < 0 else check
print(check if total >= 0 else -1)