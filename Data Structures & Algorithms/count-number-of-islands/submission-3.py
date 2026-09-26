class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        LAND = '1'
        WATER = '0'
        ROW = len(grid)
        COL = len(grid[0])
        visit = set()
        islands = 0

        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= ROW or j >= COL or grid[i][j] == '0' or grid[i][j] == "V":
                return
            grid[i][j] = "V"
            dfs(i + 1, j, grid)
            dfs(i, j + 1, grid)
            dfs(i - 1, j, grid)
            dfs(i, j - 1, grid)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == LAND and (i, j) not in visit:
                    dfs(i, j, grid)
                    islands += 1

        return islands

