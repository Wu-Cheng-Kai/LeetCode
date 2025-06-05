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
            
        self.head = root

        # if not (root.left or root.right):
        #     # self.head.right = root
        #     # self.head.left = None
        #     print(root.val)

        if root.left:
            root.left = self.search(root.left)
        if root.right:
            root.right = self.search(root.right)
        
    
    def search(self, root: TreeNode) -> TreeNode:

        print(root.val, self.head)
        a = self.head
        self.head = root

        if root.left:
            root.left = self.search(root.left)
        if root.right:
            root.right = self.search(root.right)
        
        a.right = root

        return root