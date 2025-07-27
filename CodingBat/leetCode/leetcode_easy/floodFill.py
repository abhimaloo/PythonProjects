class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        originalColor = image[sr][sc]
        if originalColor == newColor:
            return image  # Avoid infinite loop

        rows, cols = len(image), len(image[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != originalColor:
                return

            image[r][c] = newColor

            # 4 directions: down, up, right, left
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image

"""
Time & Space Complexity:
Time Complexity: O(n * m)

In the worst case, all pixels might be visited.

Space Complexity: O(n * m) in the worst case due to recursion stack in DFS"""