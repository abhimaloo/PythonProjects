class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and column to mark zeroes
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set matrix cells to 0 using markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

"""
Step-by-step explanation:
Step 1: Initialize dimensions
Get the number of rows and columns in the matrix.
Step 2: Check if first row or first column have any zeroes
We need to remember this separately because we'll later use the first row and column as markers.

Step 3: Use first row and first column to mark zero rows/columns
Traverse the matrix except the first row and column.
If matrix[i][j] is zero:
Mark the start of the row (matrix[i][0]) as zero.
Mark the start of the column (matrix[0][j]) as zero.
These marks will be used to zero out the respective rows and columns later.

Step 4: Zero out cells based on markers

for i in range(1, rows):
    for j in range(1, cols):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0
For each cell (except in the first row/column),
If either the row marker or column marker is zero,
Set the cell to zero.
Step 5: Handle first row separately if needed

if first_row_zero:
    for j in range(cols):
        matrix[0][j] = 0
If the first row originally had any zero,
Set the entire first row to zero.
Step 6: Handle first column separately if needed

if first_col_zero:
    for i in range(rows):
        matrix[i][0] = 0
If the first column originally had any zero,
Set the entire first column to zero

Summary:
The first row and column are used as markers to avoid using extra space.
First, we mark rows and columns that need to be zeroed.
Then zero all cells based on those markers.
Finally, zero the first row and/or column if they originally contained zeros.
Time and Space Complexity:
Time Complexity: O(m*n) (visit every cell a few times)
Space Complexity: O(1) (in-place, no extra space except variables)

"""