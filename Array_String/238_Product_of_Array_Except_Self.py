nums = [1,2,3,4]

# # 1. using division operation
# zero_count, product = 0, 1
# nums_len = len(nums)

# for i in nums:
#     if i == 0:
#         zero_count += 1
#     else:
#         product *= i

# if zero_count > 1:
#     result = [0] * nums_len
# elif zero_count > 0:
#     zero_index = nums.index(0)
#     result = [0] * nums_len
#     result[zero_index] = product
# else:
#     result = []
#     for i in range(nums_len):
#         result[i] = int(product/nums[i])

# 2. 
pre, post = 1, 1
nums_len = len(nums)
result = [1] * nums_len

for i in range(nums_len-1):
    pre *= nums[i]
    post *= nums[-i-1]
    result[i+1] *= pre
    result[-i-2] *= post

print(result)