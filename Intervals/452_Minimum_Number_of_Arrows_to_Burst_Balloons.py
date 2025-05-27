# 1. update target range to search
def findMinArrowShots(points: list) -> int:
    arrow = 1
    points = sorted(points, key = lambda x : x[0])
    target = points[0]

    for point in points[1:]:
        if point[0] > target[1]:
            arrow += 1
            target = point
        else:
            target = [max(target[0], point[0]), min(target[1], point[1])]

    return arrow

# 2. only update end
def findMinArrowShots1(points: list) -> int:
    arrow = 1
    points = sorted(points, key = lambda x : x[1])
    end = points[0][1]

    for point in points[1:]:
        if point[0] > end:
            arrow += 1
            end = point[1]

    return arrow

points = [[10,16],[2,8],[1,6],[7,12]]
ans = findMinArrowShots1(points)
print(ans)