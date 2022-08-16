import itertools

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
        return
    grid[i][j] = 0
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)
    
def solution(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    for i, j in itertools.product(range(m), range(n)):
        if grid[i][j] == 1:
            count += 1
            dfs(grid, i, j)
    return count

