class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            grid[r][c] = '0'  # mark visited

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc) and grid[nr][nc] == '1':
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands