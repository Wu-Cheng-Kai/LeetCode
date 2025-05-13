ratings = [1,3,4,5,2]

print(ratings)
children_num = len(ratings) 
candy, candy_sum = [1] * children_num, 0
pre, current, candy_now = -1, 0, 0

for i in range(1, children_num):
    if ratings[i] > ratings[i-1]:
        candy[i] = candy[i-1] + 1
print(candy)
for i in range(children_num-2, -1, -1):
    if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
        candy[i] = candy[i+1] + 1

print(candy)
print(sum(candy))
