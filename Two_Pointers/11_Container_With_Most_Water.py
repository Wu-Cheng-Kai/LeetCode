# 1. brute force method >> too much time
# def maxArea(height) -> int:
#     max_area = 0
#     for i in range(len(height)):
#         for j in range(i+1, len(height)):
#             area = min(height[i], height[j]) * (j - i)
#             max_area = max(area, max_area)
#     return max_area

# 2.
def maxArea(height) -> int:
    max_area, max_left, max_right = 0, 0, 0
    left, right = 0, len(height) - 1

    while left != right:
        if height[left] > max_left or height[right] > max_right:
            max_left = height[left]
            max_right = height[right]
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))