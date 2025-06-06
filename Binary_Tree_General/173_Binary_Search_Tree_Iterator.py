# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# modify tree structure: O(n) sapce
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.next_node = None
        self._forward(root)
        self.current = TreeNode(-1)
        self.current.right = self.next_node
        
    def next(self) -> int:
        self.current = self.current.right
        return self.current.val

    def hasNext(self) -> bool:
        return self.current.right != None

    def _forward(self, node: TreeNode) -> None:
        if node:
            self._forward(node.right)
            node.right = self.next_node
            self.next_node = node
            self._forward(node.left)

# stack: O(h) sapce h = the height of the tree
class BSTIterator:

    def __init__(self, root:TreeNode):
        self.stack = []
        self._get_left(root)
        self.current = TreeNode(-1)
        
    def next(self) -> int:
        self.current = self.stack.pop()
        if self.current.right:
            self._get_left(self.current.right)
        return self.current.val

    def hasNext(self) -> bool:
        return self.stack != []

    def _get_left(self, node: TreeNode) -> None:
        while node:
            self.stack.append(node)
            node = node.left
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()