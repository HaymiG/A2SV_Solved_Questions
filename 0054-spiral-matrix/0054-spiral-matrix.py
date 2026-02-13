class Solution:
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        top, bottom = 0, n - 1
        left, right = 0, m - 1

        result = []

        while left <= right and top <= bottom:
            # Traverse top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Traverse left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
