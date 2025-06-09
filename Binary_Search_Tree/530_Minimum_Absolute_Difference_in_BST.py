# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min = float('inf')
        self.list = []

        self.forward(root)
        self.list.sort()

        for i in range(1, len(self.list)):
            self.min = min(self.min, self.list[i] - self.list[i-1])

        return self.min

    def forward(self, node: TreeNode):
        if node:
            self.list.append(node.val)
            self.forward(node.left)
            self.forward(node.right)

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node):
            if node:
                inorder(node.left)

                if self.prev is not None:
                    self.min_diff = min(self.min_diff, node.val - self.prev)
                self.prev = node.val
                
                inorder(node.right)
        
        inorder(root)
        return self.min_diff