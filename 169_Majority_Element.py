nums = [2,2,1,1,1,2,2]

# # 1. set check
# min_times = len(nums) / 2
# element = set(nums)
# for i in element:
#     if nums.count(i) > min_times:
#         break

# 2. for loop check all list
min_times = len(nums) / 2
element = []

for i in nums:
    if i not in element:
        if nums.count(i) > min_times:
            break
        else:
            element.append(i)

print(i, min_times)