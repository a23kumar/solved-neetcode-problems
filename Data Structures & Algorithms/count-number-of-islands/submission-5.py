class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        
        res = 0

        def dfs(i, j, grid):
            # base case
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] in ["0", 'V']:
                return

            grid[i][j] = "V"
            dfs(i-1, j, grid)
            dfs(i, j-1, grid)
            dfs(i+1, j, grid)
            dfs(i, j+1, grid)

            return

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    res += 1
        return res