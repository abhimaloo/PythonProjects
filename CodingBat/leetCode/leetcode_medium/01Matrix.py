class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        rows, cols = len(mat), len(mat[0])
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = float('inf')

        while queue:
            r, c = queue.popleft()
            distance = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for row, col in distance:
                if 0 <= row < rows and 0 <= col < cols and mat[row][col] > mat[r][c] + 1:
                    mat[row][col] = mat[r][c] + 1
                    queue.append((row, col))
        return mat

"""
We create a queue to hold all starting points for BFS.

rows and cols store matrix dimensions.

All 0s are enqueued as BFS starting points (distance 0).

All 1s are initially set to infinity (float('inf')) to mark them as unvisited.

For each cell (r, c) dequeued:

Check its 4 neighbors (up, down, left, right).

If neighbor is within bounds and the current distance is greater than mat[r][c] + 1, update it.

Append updated neighbor to queue to continue BFS from there.

Time Complexity: O(m * n) — each cell is processed once.

Space Complexity: O(m * n) — worst-case for queue and storing distances.

"""