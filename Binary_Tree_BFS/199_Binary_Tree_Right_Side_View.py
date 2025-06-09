class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        if not root:
            return []
        
        nodes = [root]
        right_side = []

        while nodes:
            children = []
            for node in nodes:
                if node.right:
                    children.append(node.right)
                if node.left:
                    children.append(node.left)
            nodes = children

        return right_side

# DFS 
class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        self.right_side = []
        self.level, self.max_level = 0, 1
        self.forward(root)
        return self.right_side

    def forward(self, node: TreeNode):
        if node:
            self.level += 1
            if self.level == self.max_level:
                self.right_side.append(node.val)
                self.max_level += 1
            self.forward(node.right)
            self.forward(node.left)
            self.level -= 1