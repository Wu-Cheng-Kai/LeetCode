def isValidSudoku(board: list) -> bool:
    row = set()
    column = [set() for _ in range(9)]
    square = [set() for _ in range(3)]

    for i in range(9):
        for j in range(9):
            if board[i][j].isnumeric():
                if board[i][j] in row:
                    return False
                else:
                    row.add(board[i][j])

                    if board[i][j] in column[j]:
                        return False
                    else:
                        column[j].add(board[i][j])

                        n = int(j) // 3
                        if board[i][j] in square[n]:
                            return False
                        else:
                            square[n].add(board[i][j])

        if i % 3 == 2:
            square = [set() for _ in range(3)]

        row.clear()

    return True

# simplify
def isValidSudoku1(board: list) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != ".":
                if (num in rows[i] or num in cols[j] or num in squares[i // 3][j // 3]):
                    return False
                rows[i].add(num)
                cols[j].add(num)
                squares[i // 3][j // 3].add(num)
    
    return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

for _ in range(100000):
    answer = isValidSudoku1(board)

print(answer)