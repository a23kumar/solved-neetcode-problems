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
                return

            visit.add((i, j))
            area[0] += 1

            dfs(i-1, j, area)
            dfs(i, j-1, area)
            dfs(i+1, j, area)
            dfs(i, j+1, area)
            

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == LAND and (i, j) not in visit:
                    area_box = [0]
                    area = dfs(i, j, area_box)
                    max_area = max(max_area, area_box[0])

        return max_area