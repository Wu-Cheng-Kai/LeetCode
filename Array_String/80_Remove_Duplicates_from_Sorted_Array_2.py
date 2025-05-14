nums = [1,1,1,2,2,3]

# 1. for loop check
pre, k, twice = None, 0, 1
for i in range(len(nums)):        
    if nums[i] != pre:
        nums[k] = nums[i]
        pre = nums[i]
        k += 1
        twice = 1
    elif twice < 2:
        nums[k] = nums[i]
        k += 1
        twice += 1

print(k, nums[:k])