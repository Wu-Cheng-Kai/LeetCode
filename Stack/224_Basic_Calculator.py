def calculate(s: str) -> int:
    digit, first = False, True
    num, include = 0, 0
    level, op = [0], [1]
    operator = {
        "+" : 1,
        "-" : -1
    }

    for i in s:
        if i != " ":
            if i.isnumeric():
                if digit:
                    num = num * 10 + int(i)
                else:
                    digit = True
                    num = int(i)
            else:
                if digit:
                    level[include] += op.pop() * num
                    digit = False
                    first = False
                if i == "(":
                    include += 1
                    level.append(0)
                    op.append(1)
                    first = True
                elif i == ")":
                    include -= 1
                    level[include] += op.pop() * level.pop()
                else:
                    if first:
                        if i == "-":
                            op.pop()
                        first = False
                    op.append(operator[i])

            print(i, level, op)
    if digit:
        level[include] += op.pop() * num

    return sum(level)

s = " 2-1 + 2 "
ans = calculate(s)
print(ans)