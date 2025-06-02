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

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    start = new_head = ListNode(None)
    pre = ListNode(None)
    same = True

    while head:
        if head.val != pre.val:
            if not same:
                new_head.next = pre
                new_head = pre
            pre = head
            same = False
        else:
            same = True

        head = head.next

    if same:
        new_head.next = None
    else:
        new_head.next = pre

    return start.next

head = [1,1,1,2,3]
head = CreateListNode(head)

ShowListNode(deleteDuplicates(head))