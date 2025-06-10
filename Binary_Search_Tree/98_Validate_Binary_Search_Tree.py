# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None

        def inorder(node: TreeNode):
            if node:
                if not inorder(node.left):
                    return False
                if self.pre:
                    if self.pre >= node.val:
                        return False
                self.pre = node.val

                if not inorder(node.right):
                    return False
            
            return True

        return inorder(root)
