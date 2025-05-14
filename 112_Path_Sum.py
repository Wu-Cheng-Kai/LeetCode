# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def hasPathSum(root, targetSum: int) -> bool:
    def move(node, remain = targetSum):
        if node == None:    # step 1
            return False
        remain -= node.val  # step 2
        if node.left == None and node.right == None and remain == 0: # step 3
            return True 
        return move(node.left, remain) or move(node.right, remain)   # step 4
    return move(root)
    
    '''
    step1: 判斷node是不是None
    step2: 不是None代表有數值，從targetSum減去(以remain表示)
    step3: 判斷是否"底下沒有路且remain=0"
            是:代表走到底且答案符合
    step4:  否:繼續往下走
    
    當沒路且remain不等於0會繼續往下走，使node=None，在step1檢測時return False
           
    '''