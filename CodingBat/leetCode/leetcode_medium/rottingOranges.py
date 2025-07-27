from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        freshoranges, time = 0, 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshoranges += 1
                if grid[i][j] == 2:
                    q.append([i, j])

        while q and freshoranges > 0:  #BFS from all rotten oranges
            for k in range(len(q)):
                r, c = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row < 0 or row >= len(grid) or
                            col < 0 or col >= len(grid[0]) or
                            grid[row][col] != 1):
                        continue
                    else:
                        grid[row][col] = 2
                        q.append([row, col])
                        freshoranges -= 1
            time += 1

        return time if freshoranges == 0 else -1


"""Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4"""

sol = Solution()
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(sol.orangesRotting(grid))
"""
You’re given a grid:
 this is a Breadth-First Search (BFS)
0: Empty cell
1: Fresh orange
2: Rotten orange
Every minute, any fresh orange adjacent (up/down/left/right) to a rotten one also becomes rotten.
You need to return:

The minimum number of minutes until no fresh orange remains.

Return -1 if impossible to rot all fresh oranges.
Time and Space Complexity
✅ Time Complexity: O(m * n)
Each cell is visited at most once.

The grid has m * n cells total.

✅ Space Complexity: O(m * n)
Worst-case queue size is m * n (if all oranges are rotten/fresh).

Also uses space for directions and variables.

"""