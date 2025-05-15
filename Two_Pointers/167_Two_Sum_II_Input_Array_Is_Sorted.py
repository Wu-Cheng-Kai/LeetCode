# 1. brute force method >> too much time (3539 ms)
# def twoSum(numbers, target):
#     for i in range(len(numbers)):
#         ans = target - numbers[i]
#         if ans in numbers[i+1:]:
#             return [i+1, i+(numbers[i+1:].index(ans))+2]
            
# 2. search according to the sum of two campare to target (3 ms)
def twoSum(numbers, target):
    t1, t2 = 0, len(numbers) - 1
    while numbers[t1] + numbers[t2] != target:
        if numbers[t1] + numbers[t2] < target:
            t1 += 1
        else:
            t2 -= 1
    return [t1+1, t2+1]

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))