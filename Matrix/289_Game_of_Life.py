# 1. record change location
def gameOfLife(board: list) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    w, h = len(board[0]), len(board)
    change = []

    for i in range(h):
        for j in range(w):
            around = sum(board[y][x] for y in range(max((i - 1), 0), min(h, (i + 2))) for x in range(max((j - 1), 0), min(w, (j + 2)))) - board[i][j]
            if board[i][j] == 1:
                if around < 2 or around > 3:
                    change.append([i, j])
            elif around == 3:
                change.append([i, j])

    for i, j in change:
        board[i][j] = 1 - board[i][j]

    return board

# 2. in-place change
def gameOfLife1(board: list) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    w, h = len(board[0]), len(board)

    for i in range(h):
        for j in range(w):
            around = sum(board[y][x] % 2
                         for y in range(max((i - 1), 0), min(h, (i + 2))) 
                         for x in range(max((j - 1), 0), min(w, (j + 2)))) - board[i][j]
            if board[i][j] == 1:
                if around not in [2, 3]:
                    board[i][j] = 3
            elif around == 3:
                board[i][j] = 4

    for i in range(h):
        for j in range(w):
            if board[i][j] > 1:
                board[i][j] -= 3

    # 0 -> 1 ---- 4 (-3) = 1 ---- 4 % 2 = 0
    # 1 -> 0 ---- 3 (-3) = 0 ---- 3 % 2 = 1

    return board

# live:
# 0 ~ 1 live -> dead
# 2 ~ 3 live -> live
# 4 ~ 8 live -> dead
#
# dead:
# 3 live -> live

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
answer = gameOfLife1(board)
print(answer)
