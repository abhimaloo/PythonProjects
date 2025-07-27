from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start DFS from Pacific Ocean (top row and left column)
        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])          # Left edge (Pacific)
            dfs(i, cols - 1, atlantic, heights[i][cols - 1])  # Right edge (Atlantic)

        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])          # Top edge (Pacific)
            dfs(rows - 1, j, atlantic, heights[rows - 1][j])  # Bottom edge (Atlantic)

        # Intersection of cells reachable by both oceans
        result = list(pacific & atlantic)
        return result
"""
Problem Summary
You are given an m x n matrix of heights.
 Water can flow from a cell to another 
 if the neighboring cell's height is less than or equal 
 to the current cell (water only flows downhill or flat).

Pacific ocean touches the top and left edges.
Atlantic ocean touches the bottom and right edges.

🔍 Goal: Return coordinates from which water can flow to both the Pacific and Atlantic oceans.

✅ DFS Solution Explanation
🔑 Key Idea:
We’ll reverse the water flow. 
Instead of flowing from each cell to oceans, 
we start DFS from the ocean edges and mark which cells can reach each ocean.
Perform DFS from:
Pacific edge cells (top row and left column)
Atlantic edge cells (bottom row and right column)
At the end, intersect the cells that can reach both oceans.
Time and Space Complexity:
Time Complexity: O(m * n)
Each cell is visited at most twice (once for each ocean).
Space Complexity: O(m * n)
For recursion stack and visited sets.
"""