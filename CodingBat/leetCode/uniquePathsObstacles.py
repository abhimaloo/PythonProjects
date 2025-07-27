class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[j][i - 1]
                elif i > 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]






