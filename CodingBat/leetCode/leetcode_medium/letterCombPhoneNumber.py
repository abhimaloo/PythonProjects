class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitToChar = {"2": "abc",
                       "3": "def",
                       "4": "ghi",
                       "5": "jkl",
                       "6": "mno",
                       "7": "pqrs",
                       "8": "tuv",
                       "9": "wxyz"}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return result

"""
Each digit maps to a set of letters, just like on old mobile phones.
edge case 
If digits is empty, return an empty list.

Otherwise, start backtracking from index 0 with an empty string.
Base Case: If your current string is as long as the input digits, add it to the result.

Loop through each letter mapped from the current digit.

Add that letter to curStr, move to the next digit (i + 1), and repeat recursively.

Time & Space Complexity
Time Complexity: O(3^N * 4^M)

N = number of digits with 3 letters (like 2,3,4,5,6,8)

M = number of digits with 4 letters (like 7,9)

Space Complexity: O(N)

Depth of the recursion stack (one level per digit)


"""










