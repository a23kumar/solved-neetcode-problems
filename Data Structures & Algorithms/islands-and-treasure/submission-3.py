class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER = -1
        TREASURE = 0
        INF = 2147483647
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visit = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))

        counter = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in DIRECTIONS:
                    h = i + x
                    v = j + y
                    if h >= 0 and h < ROWS and v >= 0 and v < COLS and (h, v) not in visit and grid[h][v] == INF:
                        grid[h][v] = counter
                        visit.add((h, v))
                        q.append((h, v))
            counter += 1


