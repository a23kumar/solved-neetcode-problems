class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # traverse the grid and everytime we hit a "1", we perform dfs and mark all visited gridspaces with a "V"

        islands = 0

        ROW = len(grid)
        COL = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == "0" or grid[i][j] == "V":
                return

            grid[i][j] = "V"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

            return




        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands
