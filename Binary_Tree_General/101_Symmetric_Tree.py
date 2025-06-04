class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    return is_same(root.left, root.right)

def is_same(node1, node2):
    if not (node1 or node2):        
        return True
    elif node1 and node2 and node1.val == node2.val:
        return is_same(node1.left, node2.right) and is_same(node1.right, node2.left)
    return False   

    # 判斷左右兩邊同一位置的node的值，若一樣才會繼續往下
    
    '''
          總共4種可能
    None  None --> True              代表成功到底，有對稱
    None  1    --> False             只有一邊到底，沒有對稱
    1     1    --> return to child   都還沒有到底，繼續往下
    1     2    --> False             都還沒有到底，但不一樣所以沒有對稱
    
    '''