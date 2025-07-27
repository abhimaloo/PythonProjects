#O(m × n)

class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        numOfIslands = 0

        def dfs(i, j):
            if(i < 0 or i >=m or j < 0 or j >= n or grid[i][j]!= "1"):  # out of bounds or current cell is not land ('1'), stop recursion.
               return
            else:
               grid[i][j] = "0"  #Mark cell as visited (sink the land).
               dfs(i, j + 1)  # right
               dfs(i, j - 1)  # left
               dfs(i + 1, j)  # down
               dfs(i - 1, j)  # up

          #Traverse the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    numOfIslands += 1
                    dfs(i,j)

        return numOfIslands

sol = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(sol.numIslands(grid))

"""
You are given a grid of '1's (land) and '0's (water).
Each '1' can connect to another '1' horizontally or vertically, forming an island.

🔍 Your goal: Count the number of islands (groups of connected '1's).
Traverse the grid.
When you find a '1', it's a new island → increment the count.
Then use DFS to mark all connected '1's as visited ('0').
Keep searching the rest of the grid.
Time & Space Complexity
Time: O(m * n)
Every cell is visited once at most
Space: O(m * n) (worst case recursion stack in DFS for large islands)




"""






