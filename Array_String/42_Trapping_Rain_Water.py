height = [0,1,0,2,1,0,1,3,2,1,2,1]

width = len(height)
pre_l, pre_r = height[0], height[-1]
l_to_r, r_to_l = [0] * width, [0] * width
l_to_r[0] = pre_l
r_to_l[-1] = pre_r
water = 0

for i in range(1, width):
    current = height[i]
    if current < pre_l:
        l_to_r[i] = pre_l
    else:
        l_to_r[i] = current
        pre_l = current

    current = height[-i-1]
    if current < pre_r:
        r_to_l[-i-1] = pre_r
    else:
        r_to_l[-i-1] = current
        pre_r = current

for i in range(1, width-1):
    water += min(l_to_r[i], r_to_l[i]) - height[i]

print(height)
print(l_to_r)
print(r_to_l)
print([y - z if x > y else x - z for x, y, z in zip(l_to_r, r_to_l, height)])
print(water)    