class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
        if not root:
            return []
        
        nodes = [root]
        total = 0
        average = []

        while nodes:
            children = []
            n_nodes = len(nodes)
            for node in nodes:
                total += node.val
                if node.right:
                    children.append(node.right)
                if node.left:
                    children.append(node.left)
            nodes = children
            average.append(round((total / n_nodes), 5))
            total = 0

        return average