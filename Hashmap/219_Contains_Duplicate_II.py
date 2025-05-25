# 1. check duplicate length
def containsNearbyDuplicate(nums:list, k: int) -> bool:
    loc = {}
    for i, num in enumerate(nums):
        if num in loc and i - loc[num] <= k:
                return True
        loc[num] = i

    return False

# 2. only search k-length
def containsNearbyDuplicate1(nums:list, k: int) -> bool:
    num_in = set(nums[:k])
    if len(num_in) < len(nums[:k]):
         return True
    else:
        for i in range(k, len(nums)):
            if nums[i] in num_in:
                return True
            else:
                num_in.add(nums[i])
                num_in.remove(nums[i-k])

    return False

nums = [1,2,3,1,2,3]
k = 2
ans = containsNearbyDuplicate1(nums, k)
print(ans)