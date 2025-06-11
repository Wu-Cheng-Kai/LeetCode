def numIslands(grid: list) -> int:
    islands = 0
    link = {}

    def get_top(x: int, y: int) -> int:
        if x > 0:
            return grid[x-1][y]
        return 0
    
    def get_left(x: int, y: int) -> int:
        if y > 0:
            return grid[x][y-1]
        return 0
    
    def connect(x: int, y: int) -> None:
        if y not in link.setdefault(x, {x}):
            link[x].update(link.setdefault(y, {y}))
            for i in link[x]:
                link[i] = link[x]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "0":
                grid[x][y] = 0
            else:
                top, left = get_top(x, y), get_left(x, y)
                if top == 0 and left == 0:
                    islands += 1
                    grid[x][y] = islands
                elif top == 0:
                    grid[x][y] = left
                else:
                    grid[x][y] = top
                    if left != 0:
                        connect(top, left)

    seen = set()
    for key in link:
        if key not in seen:
            seen.update(link[key])
            islands -= len(link[key]) - 1
        
    return islands

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
ans = numIslands(grid)
print(ans)
