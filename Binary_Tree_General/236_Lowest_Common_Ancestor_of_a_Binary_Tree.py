class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pq = {p.val, q.val}
        self.end = False
        return self.forward(root)

    def forward(self, node: TreeNode):
        if not self.end:
            if node:
                find = self.find_pq(node.val)
                left = self.forward(node.left)
                if left not in {True, False}:
                    return left
                right = self.forward(node.right)
                if right not in {True, False}:
                    return right
                if find:
                    if left or right:
                        return node            
                    return True
                else:
                    if left and right:
                        return node
                    elif left or right:
                        return True
                    return False
        return False
            
    def find_pq(self, node_value: int) -> bool:
        if node_value in self.pq:
            self.pq.remove(node_value)
            if not self.pq:
                self.end = True
            return True
        return False