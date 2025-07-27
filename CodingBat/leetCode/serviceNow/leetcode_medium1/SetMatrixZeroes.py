class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and column to mark zeros
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

"""
✅ Problem Summary:
You're given an m x n integer matrix. If an element is 0, set its entire row and column to 0 — in place.

✅ Constraints:
Must modify the input matrix in-place.

Try to use constant space if possible.

✅ Optimal Approach (O(1) space, O(m*n) time):
Use the first row and first column as markers to remember which rows/columns need to be zeroed.

Key Points:
Don’t use extra space except a few boolean flags.

First row and column are reused as memory to track zeros.

Set values after tracking to avoid premature overwrites.
"""