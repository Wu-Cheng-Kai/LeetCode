def merge(intervals: list) -> list:
    sol = []

    while len(intervals) > 0:
        a, b = intervals.pop(0)
        check = True
        while check:
            check = False
            for i in range(len(intervals) - 1, -1, -1):
                x, y = intervals[i]
                if not (x > b or y < a):
                    a = min(a, x)
                    b = max(b, y)
                    intervals.pop(i)
                    check = True
        sol.append([a, b])
    return sol

intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = merge(intervals)
print(ans)