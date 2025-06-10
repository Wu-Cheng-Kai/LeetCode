# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.found = False
        self.count = 0
        self.target = None

        def inorder(node: TreeNode):
            if not self.found:
                if node:
                    inorder(node.left)
                    self.count += 1
                    if self.count == k:
                        self.found = True
                        self.target = node.val
                        return
                    inorder(node.right)

        inorder(root)
        return self.target