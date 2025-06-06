class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        self.order = []

        if root.left:
            self.search(root.left)
        if root.right:
            self.search(root.right)

        for node in self.order:
            root.right = node
            root.left = None
            root = node
    
    def search(self, root: TreeNode):
        self.order.append(root)
        
        if root.left:
            self.search(root.left)
        if root.right:
            self.search(root.right)

class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.pre = None

        def forward(node: TreeNode):
            if node:
                forward(node.right)
                forward(node.left)

                node.right = self.pre
                node.left = None
                self.pre = node

        forward(root)
