
def climbStairs(n: int) -> int:
    total_way = 0    # 走n步方法數
    last_way = 1     # 走n-1步方法數
    last_1 = 0       # 前1次為走一步的方法數
    for i in range(n):        # i從1~n
        total_way = last_way + last_1    # lastway:步驟1，last_1:步驟2
        last_1 = last_way
        last_way = total_way
    return total_way
  
    '''
    n=1,
    
      1
    
    n=2,
    
      11     兩個步驟: 1.將n-1步的所有方法最後面加一步
                      2.最後兩步為11時，將11換成2並新增入方法
      2
    
    n=3,
    
      111 -->步驟1
      21
      
      112 -->步驟2
    
    n=4,
    
      1111
      211
      1121
      
      1112
      22
    
    '''