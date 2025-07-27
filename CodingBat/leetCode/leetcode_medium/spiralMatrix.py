class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        left, top, right, bottom = 0, 0, n - 1, m - 1

        while top <= bottom and left <= right:
            # left to right top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # top to bottom , right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result







