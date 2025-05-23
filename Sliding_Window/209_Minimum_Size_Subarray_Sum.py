def minSubArrayLen(target: int, nums) -> int:
    current = []
    min_len, pre_len = 0, len(nums)
    now = 0
    for i in nums:
        current.append(i)
        now += i
        
        while now >= target:
            now_len = len(current)
            min_len = min(now_len, pre_len)
            pre_len = min_len
            now -= current.pop(0)

    return min_len

def minSubArrayLen1(target: int, nums) -> int:
    res = len(nums)
    sm, r, l = 0, 0, 0
    for r in range(res):
        sm += nums[r]
        while sm >= target:
            res = min(res, r-l+1)
            sm -= nums[l]
            l += 1
    return res if l > 0 else 0

target = 15
nums = [5,1,3,5,10,7,4,9,2,8]

answer = minSubArrayLen1(target, nums)
print(answer)