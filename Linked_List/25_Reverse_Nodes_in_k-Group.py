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

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    if k == 1:
        return head
    
    start = pre = ListNode(0)
    start.next = end = head
    create_head = new_end = ListNode(head.val)

    n = 1
    while head:
        if n % k == 1:
            create_head = new_end = ListNode(head.val)
            end = head
        else:
            new_head = ListNode(head.val)
            new_head.next = create_head
            create_head = new_head
        
        if n % k == 0:
            pre.next = create_head
            pre = new_end

        n += 1
        head = head.next
                 
    if n % k != 1:
        pre.next = end

    return start.next

def reverseKGroup1(head: ListNode, k: int) -> ListNode:
    if k == 1:
        return head
    
    begin = start = ListNode(0)
    start.next = head

    n = 1
    while head:
        if n % k == 1:
            pass
        elif n % k == 0:
            first = start.next
            end = head.next
            for _ in range(k - 1):
                temp1 = start.next
                temp2 = head.next
                start.next = start.next.next
                head.next = temp1
                temp1.next = temp2

            first.next = end
            head = start = first

        n += 1
        head = head.next

    return begin.next

head = [1,2,3,4,5,6,7]
head = CreateListNode(head)
k = 6
ShowListNode(reverseKGroup1(head, k))