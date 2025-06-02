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

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next:
        return head
    
    count = 0
    all_node = {}

    while head:
        all_node[count] = head
        head = head.next
        count += 1

    shift = k % count
    if shift == 0:
        return all_node[0]
    else:
        all_node[count - 1].next = all_node[0]
        all_node[count - shift - 1].next = None
        return all_node[count - shift]

head = [1,2,3,4,5]
head = CreateListNode(head)
k = 11
ShowListNode(rotateRight(head, k))