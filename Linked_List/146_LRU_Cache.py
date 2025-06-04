class LRUCache:

    def __init__(self, capacity: int):
        self.max = capacity
        self.cache = {}
        self.old = self.new = ListNode(None)

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            if key != self.new.key:
                self.forward(key)
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            if key != self.new.key:
                self.forward(key)
            self.new.val = value
        else:
            if len(self.cache.keys()) == self.max:
                self.delete()

            self.cache[key] = ListNode(key, value, self.new)
            self.new.next = self.cache[key]
            self.new = self.new.next

    def forward(self, key: int):
        self.cache[key].pre.next = self.cache[key].next
        self.cache[key].next.pre = self.cache[key].pre
        self.cache[key].pre = self.new
        self.new.next = self.cache[key]
        self.new = self.new.next
        self.new.next = None

    def delete(self):
        if self.old.next.next:
            self.old.next = self.old.next.next
            del self.cache[self.old.next.pre.key]
            self.old.next.pre = self.old
        else:
            del self.cache[self.old.next.key]
            self.new = self.old

class LRUCache1:

    def __init__(self, capacity: int):
        self.max = capacity
        self.cache = {}

        self.old = ListNode(None)
        self.new = ListNode(None)
        self.old.next = self.new
        self.new.pre = self.old

    def get(self, key: int) -> int:
        if key in self.cache:
            self._forward(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._forward(self.cache[key])
        else:
            if len(self.cache.keys()) == self.max:
                delete_node = self.old.next
                self._remove(delete_node)
                del self.cache[delete_node.key]

            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add(new_node)

    def _forward(self, node):
        self._remove(node)
        self._add(node)

    def _add(self, node):
        node.pre = self.new.pre
        node.pre.next = node
        self.new.pre = node
        node.next = self.new
    
    def _remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
            
class ListNode:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

def ShowListNode(listnode: ListNode):
    l = []
    while listnode:
        l.append(listnode.val)
        listnode = listnode.next
    print(l)

# Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache1(3)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.put(3, 3)
lRUCache.put(4, 4)
print(lRUCache.get(4))
print(lRUCache.get(3))
print(lRUCache.get(2))
lRUCache.put(5, 5)
# print(lRUCache.get(1))
print(lRUCache.get(5))
print(lRUCache.get(4))
print(lRUCache.get(3))
print(lRUCache.get(2))
print(lRUCache.get(1))