nums = [1,2]

# # 1. get all index that can jump
# now, last = 1, len(nums)
# point = {now}

# for jump in nums:
#     if last in point:
#         # return True
#         print(True)
#         break
#     elif now in point:
#         point.remove(now)
#         if jump > 0:
#             for i in range(1, jump+1):
#                 point.add(now+i)
#         elif not point:
#             # return False
#             print(False)
#             break

#         now += 1

# 2. compute cost
can_jump = 0
if len(nums) == 1:
    # return True
    print(True)
else:
    for jump in nums[:-1]:
        if jump > can_jump:
            can_jump = jump
        elif can_jump == 0:
            # return False
            print(False)
            break
        can_jump -= 1

    # return True
    print(True)


                