nums = [0,0,1,1,1,2,2,3,3,4]

# # 1. set
# nums[:] = list(set(nums))
# nums.sort()
# k = len(nums)

# 2. for loop
pre, k = None, 0
for i in range(len(nums)):
    if nums[i] != pre:
        nums[k] = nums[i]
        pre = nums[i]
        k += 1

print(k, nums[:k])