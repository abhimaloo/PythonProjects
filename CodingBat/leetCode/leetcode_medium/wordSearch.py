class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                    r >= ROWS or c >= COLS or
                    word[i] != board[r][c] or
                    (r, c) in path):
                return False

            path.add((r, c))

            result = (dfs(r + 1, c, i + 1) or
                      dfs(r - 1, c, i + 1) or
                      dfs(r, c + 1, i + 1) or
                      dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False


"""
Base case: if i has reached the end of word, the entire word has been matched.
Boundary check
Character match check
Already-visited check

Mark current cell as visited
Try all four directions from current cell
Backtrack: unmark cell so it can be reused in a different path

Try starting DFS from every cell in the board

Return True if any path finds the word

Time Complexity:
Worst case: O(N × 3^L)

N = total cells (ROWS × COLS)

L = length of word

We branch up to 3 directions per step (not 4, because we never go back)

Space Complexity:
O(L) for the recursion stack and path set






"""





