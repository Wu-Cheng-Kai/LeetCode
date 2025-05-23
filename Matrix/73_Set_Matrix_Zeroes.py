def setZeroes(matrix: list) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    x_set, y_set = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                x_set.add(i)
                y_set.add(j)

    for i in range(len(matrix)):
        if i in x_set:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        else:
            for j in range(len(matrix[0])):
                if j in y_set:
                    matrix[i][j] = 0
    
    return matrix


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
answer = setZeroes(matrix)
print(answer)