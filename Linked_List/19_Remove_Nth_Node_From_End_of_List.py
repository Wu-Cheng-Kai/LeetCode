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

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    all_node = []
    start = head

    while head:
        all_node.append(head)
        head = head.next

    if n == 1:
        if len(all_node) > 1:
            all_node[-2].next = None
        else:
            return None
    elif n == len(all_node):
        return all_node[1]
    else:
        all_node[-n - 1].next = all_node[-n + 1]

    return start

head = [1,2,3,4,5]
head = CreateListNode(head)
n = 1

ShowListNode(removeNthFromEnd(head, n))