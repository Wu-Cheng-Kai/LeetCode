def twoSum(nums, target: int):
    sol = {}
    for i in range(len(nums)):
        if nums[i] in sol:
            return [sol[nums[i]], i]
        else:
            sol[target - nums[i]] = i
            
nums = [2,7,11,15]
target = 9

answer = twoSum(nums, target)
print(answer)