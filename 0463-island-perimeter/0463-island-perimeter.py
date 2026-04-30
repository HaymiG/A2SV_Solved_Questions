class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        direction =[(-1 , 0),(1 , 0),(0 , -1),(0 , 1)]
        par = 0 
        visited = set()
        

        def dfs(r , c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return 1

            if grid[r][c] == 0:
                return 1

            if (r , c) in visited :
                return 0

            visited.add((r , c))

            par = 0

            for dr , dc in direction :
                nr , nc = r + dr , c + dc
                par +=  dfs(nr , nc)
            return par

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return dfs(r , c)
        return 0 
      
                

        