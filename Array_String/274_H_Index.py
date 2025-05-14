citations = [6, 5, 3, 1, 0]

# 1. Brute Force Method
h_index = 1
citations.sort(reverse=True)

for i in citations:
    if i < h_index:
        break
    h_index += 1

print(h_index-1)
# return h_index - 1