class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

x = [9, 9, 9, 9, 9, 9, 9]
y = [9, 9, 9, 9]

a = l1 = ListNode(None)
b = l2 = ListNode(None)
# a = l1
# b = l2

for i in range (len(x)):
    l1.next = ListNode(x[i])
    l1 = l1.next

for i in range (len(y)):
    l2.next = ListNode(y[i])
    l2 = l2.next

l1 = a.next
l2 = b.next

def print_link_list(input):
    while input:
        v = input.val
        input = input.next
        print(v, end='')
    print()

# print_link_list(l1)
# print_link_list(l2)

# s = sum_list = ListNode(None)
# n1, n10 = 0, 0
# while l1 or l2 or n10 != 0:
#     temp = 0
#     if l1 != None:
#         temp += l1.val
#         l1 = l1.next
    
#     if l2 != None:
#         temp += l2.val
#         l2 = l2.next

#     temp += n10
#     n1 = temp % 10
#     n10 = temp // 10
#     # print(temp, n1, n10)
#     sum_list.next = ListNode(n1)

#     sum_list = sum_list.next  
#     # print("s")
#     # print(sum_list.val)

# print_link_list(s.next)

s = sum_list = ListNode(None)
total = 0
scale = 1
while l1 or l2:
    if l1:
        total += l1.val * scale
        l1 = l1.next
    if l2:
        total += l2.val * scale
        l2 = l2.next
    scale *= 10
if total == 0:
    sum_list.next = ListNode(0)
else:
    while total > 0:
        sum_list.next = ListNode(total%10)
        sum_list = sum_list.next
        total = total // 10

print_link_list(s.next)
