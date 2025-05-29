class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. fast-slow
def hasCycle(head: ListNode) -> bool:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    
    return False

# 2. set   
def hasCycle(head: ListNode) -> bool:
    meet = {head.val}
    while head.next:
        head = head.next
        if head.val in meet:
            return True
        meet.add(head.val)
    
    return False

head = [3,2,0,-4]
pos = 1
