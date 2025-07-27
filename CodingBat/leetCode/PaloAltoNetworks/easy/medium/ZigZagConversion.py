"""
You are given a string s and an integer numRows.
Write the code that converts s to a zigzag pattern on numRows, and then reads the result row by row.
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curRow = 0
        goingDown = False

        for c in s:
            rows[curRow] += c

            # Reverse direction if at top or bottom
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown

            curRow += 1 if goingDown else -1

        return ''.join(rows)

"""
 Zigzag Logic:
You traverse the string character by character, 
placing each character in the appropriate row. The row index moves:
downward (row++)
then upward diagonally (row--)
and repeats...

Step-by-Step Example:
Let’s walk through "PAYPALISHIRING" with numRows = 3:
Initialize rows = ["", "", ""], curRow = 0, goingDown = False
For each character:
Add it to the current row
Change direction if needed (top/bottom row)
Move to the next row

After full traversal:

rows = [
  "PAHN",   # Row 0
  "APLSIIG",# Row 1
  "YIR"     # Row 2
]
Final result = "PAHNAPLSIIGYIR"

Time Complexity:
O(n) — One pass through s.

📦 Space Complexity:
O(n) — Storing characters in row arrays.

"""