from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        if not root:
            return []
        
        nodes = [root]
        all_value = []
        level = 0
        
        while nodes:
            level_value = []
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                level_value.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if level % 2 != 0:
                level_value.reverse()        
            all_value.append(level_value)
            level += 1

        return all_value
    
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        if not root:
            return []
        
        nodes = deque([root])
        all_value = []
        l_to_r = False

        while nodes:
            level_value = []
            for _ in range(len(nodes)):
                node = nodes.popleft()
                level_value.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if l_to_r:
                level_value.reverse()
            all_value.append(level_value)
            l_to_r = not l_to_r

        return all_value