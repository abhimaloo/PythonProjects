class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(r, c, r0, c0, shape):
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
Given a 2D grid of 0s (water) and 1s (land), find the number of distinct islands.
Two islands are considered distinct if their shapes are different, regardless of their location.
Islands are formed by connecting adjacent lands horizontally or vertically.
You need to count how many unique island shapes appear in the grid.

Approach:
Use DFS (or BFS) to traverse each island.
During traversal, record the relative positions of each cell in the island compared to the island's starting point.
Represent the shape as a tuple of relative coordinates.
Add this shape to a set to ensure uniqueness.
The size of the set at the end is the number of distinct islands.

 Explanation:
For each unvisited land cell, do DFS.
Capture the shape by relative coordinates (r - r0, c - c0).
Using relative coordinates normalizes the position so islands that are same shape but in different locations are considered the same.
Keep shapes in a set to avoid duplicates


Time Complexity:
O(m × n) — we visit each cell once.

📦 Space Complexity:
O(m × n) for recursion stack and visited set.
"""