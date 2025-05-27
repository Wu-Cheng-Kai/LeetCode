# while loop to check overlap
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

# 2. sort by interval[0] first
def merge1(intervals: list) -> list:
    sol = []

    intervals = sorted(intervals, key = lambda x : x[0])

    a, b = intervals[0]
    for interval in intervals[1:]:
        if interval[0] <= b:
            b = max(interval[1], b)
        else:
            sol.append([a, b])
            a, b = interval
    sol.append([a, b])

    return sol

intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = merge1(intervals)
print(ans)