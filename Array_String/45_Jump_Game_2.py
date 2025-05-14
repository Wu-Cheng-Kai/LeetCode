nums = [2,3,1,1,4,5]

# # 1. check minimum times can reach each index (double for-loop)
# now, last = 0, len(nums)-1
# jump_times = [0] * len(nums)

# for i in range(last):
#     print(jump_times)
#     jump_times_current = jump_times[now]
#     for j in range(1, nums[i]+1):
#         if now+j <= last:
#             if jump_times_current+1 < jump_times[now+j] or jump_times[now+j] == 0:
#                 jump_times[now+j] = jump_times_current+1
#     now += 1

# 2. record farthest index
now, last = 0, len(nums)-1
jump_times, farthest = 0, 0

for i in range(last):
    farthest = max(farthest, i+nums[i])
    if i == now:
        jump_times += 1
        now = farthest
    print(i, farthest, jump_times)

print(jump_times)
# print(jump_times[-1])