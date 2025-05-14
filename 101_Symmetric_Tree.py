# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(root) -> bool:
    def TorF(tree1, tree2):
        if tree1 == None and tree2 == None:        
            return True
        elif not(tree1 == None or tree2 == None):
            if tree1.val == tree2.val:
                return TorF(tree1.left, tree2.right) and TorF(tree1.right, tree2.left)
        return False   
    return TorF(root.left, root.right)

    # 判斷左右兩邊同一位置的node的值，若一樣才會繼續往下
    
    '''
          總共4種可能
    None  None --> True              代表成功到底，有對稱
    None  1    --> False             只有一邊到底，沒有對稱
    1     1    --> return to child   都還沒有到底，繼續往下
    1     2    --> False             都還沒有到底，但不一樣所以沒有對稱
    
    '''