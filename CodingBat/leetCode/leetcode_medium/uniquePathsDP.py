class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # intialize the 2d dp table with 1s
        dp = [[1] * n for _ in range(m)]

        # fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]

"""
Create a 2D list dp with m rows and n columns.

Initialize all cells with 1 because:

The first row has only 1 path (moving right only).
The first column has only 1 path (moving down only).

For every other cell (i, j), the number of ways to get there is:

Number of ways to get to the cell to the left (i, j-1), plus

Number of ways to get to the cell above (i-1, j)

This is because you can only move right or down.
Return the value at the bottom-right corner — total unique paths to reach the destination.
Metric	Value
Time	O(m * n)
Space	O(m * n)

"""









