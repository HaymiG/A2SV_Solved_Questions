class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row  = len(grid)
        col = len(grid[0])
        p = 0
        visited = set()
        
        def dfs(r , c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return 1

            if grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r , c))
            direction = [(0 , -1), (0 , 1), (1,0),(-1 , 0)]
            par = 0

            for x, y in direction:
                par += dfs(r + x, c + y)
                        
            
            return par
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r, c) 
        return 0







        