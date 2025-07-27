class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []   #will store all valid combinations.
        digitToChar = {"2": "abc",
                       "3": "def",
                       "4": "ghi",
                       "5": "jkl",
                       "6": "mno",
                       "7": "pqrs",
                       "8": "tuv",
                       "9": "wxyz"}
        #A dictionary that maps each digit to the characters it represents on a phone keypad.

        #This is the recursive function to build combinations.
        #i = currentindex in digits
         #curStr = currently built string

        def backtrack(i, curStr):
            if len(curStr) == len(digits):   #📌 Base Case:
                result.append(curStr)
                return

            for c in digitToChar[digits[i]]:  #📌 Recursive Case:
                backtrack(i + 1, curStr + c)
                #Get the letters for digits[i]
                #For each letter c, add it to current string and recurse for next digit

        if digits:
            backtrack(0, "")   #4. Starting Condition:If digits is not empty, start backtracking.

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
📘 Example:
Let’s walk through digits = "23"
"2" → "abc"
"3" → "def"
So we want all combinations of one letter from "abc" followed by one from "def".
backtrack(0, "") → digit = "2" → letters = "abc"
 └─ a → backtrack(1, "a") → digit = "3" → letters = "def"
      ├─ d → backtrack(2, "ad") ✅
      ├─ e → backtrack(2, "ae") ✅
      └─ f → backtrack(2, "af") ✅
 └─ b → backtrack(1, "b") → same...
      ├─ d → "bd" ✅
      ├─ e → "be" ✅
      └─ f → "bf" ✅
 └─ c → same...
      ├─ "cd" ✅
      ├─ "ce" ✅
      └─ "cf" ✅
✅ Final result:

["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

"""










