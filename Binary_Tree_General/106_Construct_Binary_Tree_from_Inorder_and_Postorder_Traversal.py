class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        self.max = len(inorder)
        self.idx = self.max - 1
        self.val_to_idx = {val: idx for idx, val in enumerate(inorder)}
        self.postorder = postorder

        return self.createNode(0, self.max)
    
    def createNode(self, left: int, right: int) -> TreeNode:
        if right <= left or self.idx < 0:
            return None
        val = self.postorder[self.idx]
        node = TreeNode(val)
        self.idx -= 1

        idx = self.val_to_idx[val]
        node.right = self.createNode(idx+1, right)
        node.left = self.createNode(left, idx)

        return node