def spiralOrder(matrix: list) -> list:
    path = []
    h, w, h_s, w_s = len(matrix), len(matrix[0]), 0, 0
    x, y = 0, 0
    d_x, d_y = 1, 0

    for i in range(w * h):
        if x == w - 1 and d_x > 0:
            d_x, d_y = 0, 1
            h_s += 1
        elif y == h - 1 and d_y > 0:
            d_x, d_y = -1, 0
            w -= 1
        elif x == w_s and d_x < 0:
            d_x, d_y = 0, -1
            h -= 1
        elif y == h_s and d_y < 0:
            d_x, d_y = 1, 0
            w_s += 1

        path.append(matrix[y][x])
        x += d_x
        y += d_y

    return path

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
answer = spiralOrder(matrix)
print(answer)