class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    copy = {}
    h = head
    c = copy_next = copy_random = Node(0)
    while head:
        copy_next.next = Node(head.val)
        copy[head] = copy_next
        copy_next = copy_next.next
        head = head.next

    copy_random = copy_random.next
    while h:
        if h.random:
            copy_random.random = copy[h.random]
        h = h.next
        copy_random = copy_random.next

    return c.next