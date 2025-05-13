s = "Hello World"

# 1.
length = len(s.split()[-1])

# 2.
# start, length = False, 0
# for i in range(len(s)):
#     if start:
#         if s[-i-1] == " ":
#             return length
#         else:
#             length += 1
#     elif s[-i-1] == " ":
#         start = True

print(length)
# return len(word[-1])