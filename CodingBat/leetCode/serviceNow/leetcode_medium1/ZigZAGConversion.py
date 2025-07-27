class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        #If only one row or numRows is greater than or equal to the length of s, zigzag isn't needed — return original string.

        rows = [''] * numRows #Create a list of empty strings, one for each row, to store characters.
        curRow = 0             #curRow tracks the current row index.
        goingDown = False      #goingDown indicates the direction: True for down, False for up.

        for c in s:   #Traverse the string:
            rows[curRow] += c      #Place each character in the correct row based on current direction.

            # Reverse direction if at top or bottom
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown         #Flip the direction when reaching the top row (0) or bottom row (numRows - 1).

            curRow += 1 if goingDown else -1      #Move to the next row based on direction.

        return ''.join(rows)    #Combine all row strings to get the final zigzagged result.
