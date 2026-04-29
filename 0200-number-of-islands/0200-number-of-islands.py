class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [(1 , 0) , (-1 , 0 ), (0 , -1) , (0 , 1)]
        island = 0 
        
        def inbound(nr , nc):
            return  0 <= nr < row and 0 <= nc < col


        def dfs( r , c):
            
            grid[r][c] = "0"

            for dr , dc in directions:
                nr = r + dr
                nc = c + dc

                if inbound(nr, nc) and grid[nr][nc] == "1":
                    dfs( nr , nc)
        

        for r in range(row ):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r , c)
                    island += 1
        return island