nums = [0,1,2,2,3,0,4,2] 
val = 2

# # 1. simple method
# while val in nums:
#     nums.remove(val)

# # 2. replace
# k = 0
# for i in nums:
#     if i != val:
#         nums[k] = i
#         k += 1

# 3. delete
k = 0
while k < len(nums):
    if nums[k] == val:
        nums.pop(k)
    else:
        k += 1

print(k, nums)