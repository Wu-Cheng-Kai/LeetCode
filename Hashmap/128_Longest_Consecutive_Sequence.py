def longestConsecutive(nums: list) -> int:
    if nums:
        nums.sort()
        max_len, strike = 1, 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff <= 1:
                strike += diff
            else:
                strike = 1
            if strike > max_len:
                max_len = strike
        return max_len
    else:
        return 0


nums = [0,3,7,2,5,8,4,6,0,1]
ans = longestConsecutive(nums)
print(ans)