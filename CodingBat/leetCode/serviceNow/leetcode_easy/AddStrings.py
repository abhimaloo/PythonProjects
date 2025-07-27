class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        return ''.join(reversed(result))
"""
✅ Problem Summary
You are given two non-negative numbers as strings, num1 and num2.
You must add them without converting the entire string to an integer directly 
(i.e., don’t use int() or big integers), and return the result as a string.
🔍 Example
Input:

num1 = "11"
num2 = "123"
Output:

"134"
🧠 Intuition
Start adding digits from right to left (like manual addition).
Keep track of the carry (if sum of digits is 10 or more).
Move leftward, digit by digit, until both strings are processed.
At the end, if there’s still a carry, add it.

"""