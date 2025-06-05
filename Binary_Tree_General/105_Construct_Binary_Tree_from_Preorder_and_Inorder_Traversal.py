class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def buildTree(self, preorder: list, inorder: list) -> TreeNode:
#         root = TreeNode(preorder[0])
#         idx = inorder.index(preorder[0])
#         preorder = preorder[1:]

#         left = inorder[:idx]
#         right = inorder[idx+1:]
#         if left:
#             root.left, preorder = createNode(preorder, left)
#         if right:
#             root.right, preorder = createNode(preorder, right)

#         return root
    
# def createNode(preorder: list, inorder: list):
#     root = TreeNode(preorder[0])
#     idx = inorder.index(preorder[0])
#     preorder = preorder[1:]

#     left = inorder[:idx]
#     right = inorder[idx+1:]
#     if left:
#         root.left, preorder = createNode(preorder, left)
#     if right:
#         root.right, preorder = createNode(preorder, right)

#     return root

class Solution1:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        self.idx = 0
        self.max = len(inorder)
        self.val_to_idx = {val: idx for idx, val in enumerate(inorder)}
        self.preorder = preorder

        return self.createNode(0, self.max)
    
    def createNode(self, left: int, right: int) -> TreeNode:
        if right <= left or self.idx >= self.max:
            return None
        val = self.preorder[self.idx]
        node = TreeNode(val)
        self.idx += 1

        idx = self.val_to_idx[val]
        node.left = self.createNode(left, idx)
        node.right = self.createNode(idx+1, right)

        return node