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

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if left == right:
        return head
    else:
        pos = 1
        h_start = head

        while head:
            if pos == left - 1:
                cut1 = head
            elif pos == left:
                h = new_head = ListNode(head.val)
            elif pos == right + 1:
                h.next = head
                if left > 1:
                    cut1.next = new_head
                    return h_start
                else:
                    return new_head


            if right >= pos > left:
                temp = new_head
                new_head = ListNode(head.val)
                new_head.next = temp

            head = head.next
            pos += 1

        if left > 1:
            cut1.next = new_head
            return h_start
        else:
            return new_head

# 2.       
def reverseBetween1(head: ListNode, left: int, right: int) -> ListNode:
    if left == right:
        return head
    
    pre_head = ListNode(0)
    pre_head.next = head
    get_head = pre_head
    
    for _ in range(left - 1):
        pre_head = head
        head = head.next

    next_head = head.next
    pre = head
    
    for _ in range(right - left):

        # head(>1 node) --> next
        # next --> head(>1 node)
        head.next = next_head.next
        next_head.next = pre
        pre = next_head
        next_head = head.next

    pre_head.next = pre
    ShowListNode(pre_head)

    return get_head.next
    
head = [1,2]
head = CreateListNode(head)
left = 1
right = 2
ShowListNode(reverseBetween1(head, left, right))