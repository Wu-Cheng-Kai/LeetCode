from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []
        
        nodes = [root]
        all_value = []
        
        while nodes:
            level_value = []
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                level_value.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            all_value.append(level_value)

        return all_value
    
class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []
        
        nodes = deque([root])
        all_value = []
        

        while nodes:
            level_value = []
            for _ in range(len(nodes)):
                node = nodes.popleft()
                level_value.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            all_value.append(level_value)

        return all_value