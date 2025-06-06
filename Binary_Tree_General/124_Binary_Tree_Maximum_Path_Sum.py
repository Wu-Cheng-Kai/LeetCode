# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = int('-inf')

        def forward(node: TreeNode) -> int:
            if not node:
                return 0
            left = max(forward(node.left), 0)
            right = max(forward(node.right), 0)
            self.max = max(self.max, node.val + left + right)
            return node.val + max(left, right)   

        forward(root)
        return self.max

