class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        result = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        result[rows][cols - 1] = 0  # dummy bottom-right neighbor

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                result[r][c] = grid[r][c] + min(result[r + 1][c], result[r][c + 1])

        return result[0][0]


"""
Approach: Dynamic Programming (Bottom-Up)
We create a DP table (result) where each cell result[r][c] 
represents the minimum path sum from cell (r, c) to the destination.

We fill this table starting from the bottom-right.
We create a (rows + 1) x (cols + 1) DP table filled with infinity
Why extra row & column? To simplify boundary conditions
We set result[rows-1][cols] = 0 so that the last cell (rows-1, cols-1) 
can correctly compute its min using min(result[r+1][c], result[r][c+1]).
But here, you "seed" the cell to the right of the bottom-right as 0
This is a trick to make the bottom-right cell work correctly.

We iterate from bottom-right backwards

For each cell (r, c):

We add the current grid value grid[r][c]

To the minimum path sum of the cell to the right or the cell below
The top-left cell now holds the minimum path sum from start to end



"""