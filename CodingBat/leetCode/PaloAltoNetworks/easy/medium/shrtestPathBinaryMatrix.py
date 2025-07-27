from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1  # start or end blocked

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = set((0, 0))

        while queue:
            r, c, dist = queue.popleft()
            if (r, c) == (n - 1, n - 1):
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    queue.append((nr, nc, dist + 1))
                    visited.add((nr, nc))

        return -1  # no path found
"""
Approach: Breadth-First Search (BFS)
Why BFS?
It explores level-by-level.
The first time you reach the destination → it's the shortest path.
BFS	Guarantees shortest path by layer-wise traversal
8 Directions	
Allows diagonal movement as well
Edge Check	
If grid[0][0] or grid[n-1][n-1] is 1 → return -1

Visited Set	Prevents cycles and re-visiting nodes
Time: O(n²) — every cell visited once at most
Space: O(n²) — for queue and visited set



"""