def summaryRanges(nums: list) -> list:
    sol = []

    if nums:
        start = end = nums[0]

        for i in nums[1:]:
            if i - 1 != end:
                if start == end:
                    sol.append(str(start))
                else:
                    sol.append(str(start) + "->" + str(end))
                start = end = i
            else:
                end = i
                
        if start == end:
            sol.append(str(start))
        else:
            sol.append(str(start) + "->" + str(end))
    else:
        return sol

nums = [0,1,2,4,5,7]
ans = summaryRanges(nums)
print(ans)