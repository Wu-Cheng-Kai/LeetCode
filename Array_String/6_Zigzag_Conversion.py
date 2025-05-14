def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    else:
        row = []
        current, direction = 0, 1

        for _ in range(numRows):
            row.append([])

        for char in s:
            row[current].append(char)
            current += direction

            if current == 0 and direction == -1:
                direction = 1
            elif current == numRows - 1 and direction == 1:
                direction = -1

        z_s = ""
        for i in row:
            z_s += "".join(i)

        return z_s

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))