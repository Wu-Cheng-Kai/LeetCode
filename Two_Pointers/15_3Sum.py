# 1. save all solution to check >> time out
def threeSum(nums):
    ans, history = [], []
    sum2, length = 0, len(nums)
    for i in range(length-2):
        sum2 = -nums[i]
        for j in range(i+1, length-1):
            if sum2 - nums[j] in nums[j+1:] and {nums[i], nums[j], sum2 - nums[j]} not in history:
                ans.append([nums[i], nums[j], sum2 - nums[j]])
                history.append({nums[i], nums[j], sum2 - nums[j]})
    return ans

# 2. category and use set
def threeSum1(nums):
    ans = []
    positive, negative, zero = [], [], []

    # category positive, negative, zero
    for num in nums:
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
        else:
            zero.append(num)

    p, n = set(positive), set(negative)

    # a.[0, 0, 0]
    if len(zero) >= 3:
        ans.append([0, 0, 0])

    # b.[x, y, 0]
    if zero:
        for i in p:
            if -i in n:
                ans.append([i, -i, 0])

    # c.[x, y, z]
    # c-1.[+, +, -]
    for third in n:
        p_set = p.copy()
        while p_set:
            first = p_set.pop()
            res = -(first + third)
            if res > 0:
                if res == first and positive.count(first) >= 2:
                    ans.append([first, res, third])
                elif res in p_set:
                    ans.append([first, res, third])
                    p_set.remove(res)

    # c-2.[-, -, +]
    for third in p:
        n_set = n.copy()
        while n_set:
            first = n_set.pop()
            res = -(first + third)
            if res < 0:
                if res == first and negative.count(first) >= 2:
                    ans.append([first, res, third])
                elif res in n_set:
                    ans.append([first, res, third])
                    n_set.remove(res)

    return ans

nums = [-1,0,1,2,-1,-4]
answer = threeSum1(nums)
print(answer, len(answer))
