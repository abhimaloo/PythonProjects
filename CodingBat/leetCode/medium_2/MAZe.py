from collections import deque

class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([start])
        visited[start[0]][start[1]] = True

        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                return True

            for dx, dy in directions:
                nx, ny = x, y

                # Roll the ball until it hits a wall or boundary
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        return False
"""
Approach: BFS or DFS with Rolling Logic
Use BFS or DFS to explore the maze.

From the current position, roll the ball in all four directions until hitting a wall.

Add the stopping position to the queue or recursion if not visited.

Repeat until reaching the destination or running out of options.
Time Complexity:
O(m * n), since each cell is visited at most once.

📦 Space Complexity:
O(m * n) for the visited array and queue.
"""
