class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return is_leaf(root, 1)
        return 0

def is_leaf(node, depth):
    if not node.right and not node.left:
        return depth
    else:
        depth += 1
        left_depth = is_leaf(node.left, depth) if node.left else depth    
        right_depth = is_leaf(node.right, depth) if node.right else depth

        return max(left_depth, right_depth)

# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        nodes = [root]
        depth = 0

        while nodes:
            depth += 1
            children = []
            for node in nodes:
                if node.right:
                    children.append(node.right)
                if node.left:
                    children.append(node.left)
            nodes = children

        return depth