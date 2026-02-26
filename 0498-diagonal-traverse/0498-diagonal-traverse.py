class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        diagonal = defaultdict(list)

        for i in range(n):
            for j in range(m):
                diagonal[i + j].append(mat[i][j])
        result = []
        for i in range(m + n -1): 
            if i % 2 == 0:
                diagonal[i].reverse()
            result.extend(diagonal[i])
        return result


        