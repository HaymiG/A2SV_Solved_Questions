class Solution(object):
    def solveNQueens(self, n):
       
        cols = [False] * n
        posDiag = [False] * (2*n - 1)
        
        negDiag = [False] * (2*n - 1)
        
        
        board = [["."] * n for _ in range(n)]
        result = []
        
        def backtrack(r):
            
            if r == n:
                
                result.append(["".join(row) for row in board])
                return
            
            
            for c in range(n):
                posD = r - c  
                negD = r + c 
                
                
                if cols[c] or posDiag[posD] or negDiag[negD]:
                    continue
                
                
                cols[c] = posDiag[posD] = negDiag[negD] = True
                board[r][c] = "Q"
                
                
                backtrack(r + 1)
                
               
                cols[c] = posDiag[posD] = negDiag[negD] = False
                board[r][c] = "."
        
        
        backtrack(0)
        return result
