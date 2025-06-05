class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        nodes = [root]

        while nodes:
            children = []
            pre_node = None
            for node in nodes:
                node.next = pre_node
                pre_node = node
                if node.right:
                    children.append(node.right)
                if node.left:
                    children.append(node.left)
            nodes = children

        return root
    
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        head = root

        while head:
            pre_node = None
            c = children = Node(pre_node)
            while head:
                head.next = pre_node
                pre_node = head
                if head.left:
                    children.next = head.left
                    children = children.next
                if head.right:
                    children.next = head.right
                    children = children.next
                head = head.next
            head = c.next

        return root