class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
        return root
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            invert = TreeNode(root.val)
            if root.right:
                invert.left = self.invertTree(root.right)
            if root.left:
                invert.right = self.invertTree(root.left)
            return invert
        else:
            return root