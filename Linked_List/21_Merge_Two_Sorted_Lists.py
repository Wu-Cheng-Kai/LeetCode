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

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    m = merge = ListNode(None)

    while list1 and list2:
        if list1.val < list2.val:
            merge.next = ListNode(list1.val)
            list1 = list1.next
        else:
            merge.next = ListNode(list2.val)
            list2 = list2.next
        merge = merge.next

    if list1:
        merge.next = list1
    elif list2:
        merge.next = list2

    return m.next

list1 = [1,2,4]
list2 = [1,3,4]

list1 = CreateListNode(list1)
list2 = CreateListNode(list2)

ShowListNode(mergeTwoLists(list1, list2))