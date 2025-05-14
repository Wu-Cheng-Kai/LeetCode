nums = [1,2,3,4,5,6,7]
k = 9

shift = k % len(nums)

# temp = nums[-shift:]
# nums[shift:] = nums[:-shift]
# nums[:shift] = temp

nums[:] = nums[-shift:] + nums[:-shift]

print(shift, nums)