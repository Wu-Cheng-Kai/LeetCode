# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0

        def forward(node: TreeNode, pre):
            pre = pre * 10 + node.val
            if not (node.left or node.right):
                self.sum += pre
            else:
                if node.left:
                    forward(node.left, pre)
                if node.right:
                    forward(node.right, pre)

        forward(root, 0)
        return self.sum