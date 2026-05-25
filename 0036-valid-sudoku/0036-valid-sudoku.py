class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if b[r][c] == ".":
                    continue
                if(b[r][c] in row[r] or b[r][c] in col[c] or b[r][c] in square[(r//3 , c//3)] ):
                    return False
                row[(r)].add(b[r][c])
                col[(c)].add(b[r][c])
                square[(r//3 ,c//3)].add(b[r][c])
        return True
