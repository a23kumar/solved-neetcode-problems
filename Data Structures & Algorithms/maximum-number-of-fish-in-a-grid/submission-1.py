class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0

        ROW = len(grid)
        COL = len(grid[0])

        visit = set()

        def dfs(i, j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == 0 or (i, j) in visit:
                return 0
            visit.add((i, j))    
            return grid[i][j] + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] > 0 and (i, j) not in visit:
                    res = max(res, dfs(i, j))

        return res
