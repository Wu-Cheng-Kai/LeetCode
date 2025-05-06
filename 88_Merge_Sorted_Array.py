nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

# # 1. simple method
# nums1[m:] = nums2
# nums1.sort()

# 2. sort two list
if m == 0:
    nums1[:] = nums2
elif n != 0:
    i, idx1, idx2 = 1, m-1, n-1
    while idx2 >= 0:
        if nums1[idx1] >= nums2[idx2]:
            nums1[-i] = nums1[idx1]
            idx1 -= 1
        else:
            nums1[-i] = nums2[idx2]
            idx2 -= 1
        i += 1
        if idx1 < 0:
            nums1[:idx2+1] = nums2[:idx2+1]
            break

print(nums1)