def insert(intervals: list, newInterval: list) -> list:
    sol = []
    done = False

    if intervals:
        for i, interval in enumerate(intervals):
            if not done:
                if interval[1] < newInterval[0]:
                    sol.append(interval)
                else:
                    if interval[0] > newInterval[1]:
                        sol.append(newInterval)
                        sol += intervals[i:]
                        break
                    else:
                        newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
                        done = True
            else:
                if newInterval[1] >= interval[0]:
                    newInterval[1] = max(newInterval[1], interval[1])
                else:
                    sol.append(newInterval)
                    sol += intervals[i:]
                    break
        else:
            sol.append(newInterval)
    else:
        return newInterval

    return sol

intervals = [[1,3],[6,9]]
newInterval = [2,5]
ans = insert(intervals, newInterval)
print(ans)