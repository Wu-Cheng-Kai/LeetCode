# 1. use another list to save
def rotate(matrix: list) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m.append(matrix[i][j])

    n = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[j][-i-1] = m[n]
            n += 1

    return matrix

# 2. in-place modify
def rotate1(matrix: list) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix_len = len(matrix)
    for i in range(matrix_len):
        for j in range(i, matrix_len):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(matrix_len // 2):
        for j in range(matrix_len):
            temp = matrix[j][i]
            matrix[j][i] = matrix[j][matrix_len - i - 1]
            matrix[j][matrix_len - i - 1] = temp

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
answer = rotate1(matrix)
print(answer)