class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_len = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(
                        dp[i - 1][j],       # top
                        dp[i][j - 1],       # left
                        dp[i - 1][j - 1]    # top-left
                    ) + 1
                    max_len = max(max_len, dp[i][j])

        return max_len * max_len




"""
Key Idea: Dynamic Programming
For each cell (i, j) in the matrix, if it's a '1', we look at the minimum of the three adjacent squares:

Top dp[i-1][j]

Left dp[i][j-1]

Top-left diagonal dp[i-1][j-1]

Then we add 1 to it — that becomes the largest square ending at that point.


dp[i][j] means the side length of the largest square ending at (i-1, j-1) in the original matrix.

We use a dp table that is 1 row and column larger to avoid index errors.

Time and Space Complexity:
Metric	Value
Time	O(m × n)
Space	O(m × n)


"""