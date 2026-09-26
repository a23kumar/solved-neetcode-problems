class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        WATER = 0
        LAND = 1
        max_area = 0
        visit = set()

        ROW = len(grid)
        COL = len(grid[0])

        def dfs(i, j, area):
            if i < 0 or j < 0 or i >= ROW or j >= COL or grid[i][j] == WATER or (i, j) in visit:
                return 0

            visit.add((i, j))

            return (1 + dfs(i-1, j, area)
            + dfs(i, j-1, area)
            + dfs(i+1, j, area)
            + dfs(i, j+1, area)
            )
            

        for i in range(ROW):
            for j in range(COL):
                area = dfs(i, j, 0)
                max_area = max(max_area, area)

        return max_area