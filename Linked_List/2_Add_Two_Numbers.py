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

# 1.
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    s = sum_list = ListNode(None)
    total = 0

    while l1 or l2:
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        sum_list.next = ListNode(total % 10)
        sum_list = sum_list.next
        total = total // 10

    if total > 0:
        sum_list.next = ListNode(total)

    return s.next

# 2.
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
