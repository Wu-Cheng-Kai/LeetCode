class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def CreateListNode(list: list) -> ListNode:
    s = l = ListNode(None)
    if list:
        for i in list:
            l.next = ListNode(i)
            l = l.next
    return s.next

def ShowListNode(listnode: ListNode):
    l = []
    while listnode:
        l.append(listnode.val)
        listnode = listnode.next
    print(l)

# create 2 (< and >=)
def partition(head: ListNode, x: int) -> ListNode:
    if not head or not head.next:
        return head
    
    l = large = ListNode(0)
    s = small = ListNode(0)
    while head:
        if head.val < x:
            small.next = head
            small = small.next
        else:
            large.next = head
            large = large.next
        head = head.next

    large.next = None
    small.next = l.next

    return s.next

# create 1 (<) and modify 1 (>=)
def partition1(head: ListNode, x: int) -> ListNode:
    if not head or not head.next:
        return head
    
    p = pre = ListNode(0)
    pre.next = head
    s = small = ListNode(0)
    while head:
        if head.val < x:
            small.next = head
            small = small.next
            pre.next = head.next
        else:
            pre = head
        head = head.next

    small.next = p.next

    return s.next

head = [1,4,3,2,5,2]
head = CreateListNode(head)
x = 4
ShowListNode(partition1(head, x))