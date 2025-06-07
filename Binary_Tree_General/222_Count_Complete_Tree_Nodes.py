class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(log^2 N) compare the depth of node.right and node.left
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.num = 0
        self.depth, self.last = 0, 0
        while root:
            left = self.get_depth(root.left)
            right = self.get_depth(root.right)
            if left == right:
                root = root.right
                if root:
                    self.last += 2 ** (right - 1)
                else:
                    break
            else:
                root = root.left
            self.depth += 1
        return 2 ** self.depth + self.last
            
    def get_depth(self, node: TreeNode) -> int:
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth 

# set flag to check is_leaf and depthest
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.depth = 0
        self.depth_max = 0
        self.single = 0
        self.end = False
        self.depthest = False

        if root:
            self.forward(root)
            return 2 ** (self.depth_max - 1) + self.single - 1
        return 0

    def forward(self, node: TreeNode):
        if not self.end:
            if not node:
                return False

            self.depth += 1
            if not (self.forward(node.left) and self.forward(node.right)):
                if not self.depthest:
                    self.find_depthest()
                elif self.is_leaf():
                    self.single += 1
                else:
                    self.end = True
            self.depth -= 1    
            return True
    
    def is_leaf(self):
        return self.depthest and self.depth_max == self.depth
    
    def find_depthest(self):
        self.depthest = True
        self.depth_max = self.depth
        self.single += 1

# DFS O(n)        
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.num = 0

        self.forward(root)
        return self.num

    def forward(self, node: TreeNode):
        if node:
            self.num += 1
            self.forward(node.left)
            self.forward(node.right)