def longestConsecutive(nums: list) -> int:
    if nums:
        nums.sort()
        max_len, streak = 1, 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff <= 1:
                streak += diff
            else:
                streak = 1
            if streak > max_len:
                max_len = streak
        return max_len
    else:
        return 0

def longestConsecutive1(nums: list) -> int:
    if nums:
        check, streak = {}, 1
        for i in nums:
            if i not in check:
                i_max = check[i + 1][0] if i + 1 in check else i
                i_min = check[i - 1][1] if i - 1 in check else i
                check[i] = [i_max, i_min]
                check[i_max] = [i_max, i_min]
                check[i_min] = [i_max, i_min]
                streak = max(streak, i_max - i_min + 1)
        return streak

    else:
        return 0

nums = [0,3,7,2,5,8,4,6,0,1]
ans = longestConsecutive1(nums)
print(ans)