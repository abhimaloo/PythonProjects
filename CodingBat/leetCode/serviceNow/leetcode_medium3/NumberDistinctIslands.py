class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(r, c, r0, c0, shape):   #(r0, c0) is the origin of the island.
            if (0 <= r < rows and 0 <= c < cols and
                grid[r][c] == 1 and (r, c) not in visited):
                visited.add((r, c))
                shape.append((r - r0, c - c0))  # relative position
                # Explore neighbors
                dfs(r + 1, c, r0, c0, shape)
                dfs(r - 1, c, r0, c0, shape)
                dfs(r, c + 1, r0, c0, shape)
                dfs(r, c - 1, r0, c0, shape)

        rows, cols = len(grid), len(grid[0])
        visited = set()
        shapes = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    shape = []
                    dfs(r, c, r, c, shape)
                    shapes.add(tuple(shape))  # add shape as immutable tuple

        return len(shapes)

"""
Your implementation of Leetcode 694: Number of Distinct Islands is excellent — 
it correctly uses DFS + relative coordinates to identify island shapes, and stores them as immutable tuples to count unique island shapes.

Here’s a breakdown of what you’ve done right and why it works:
Problem Summary
Given a grid of 0s (water) and 1s (land), count the number of distinct islands.

Two islands are considered distinct if their shapes (relative positions of land cells) are different,
 regardless of location in the grid.
 
 For each DFS visit, you store (r - r0, c - c0) — the relative coordinate — 
 so identical shapes will match even if their position differs.
 
 The shape is a list of relative positions, 
 which you convert to a tuple so it can be added to a set (to deduplicate).

This ensures that identical shapes (regardless of location) are only counted once.

grid = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,0,1,1],
  [0,0,0,1,1]
]
There are 2 islands of the same shape (2×2 square). The relative shape for both is:

[(0,0), (0,1), (1,0), (1,1)]
Your code will count 1 distinct island shape — correct!

Time and Space Complexity
Time: O(m * n) — visit each cell once
Space:
O(m * n) for visited set and recursion stack
Up to O(m * n) shapes in the worst case

"""