class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))

"""Explanation:
We initialize two pointers, i and j, at the end of strings a and b.
carry keeps track of the carry-over during addition (either 0 or 1).
We loop while either string has digits left or there is a carry.
At each step:
Add the current digits (if available) and the carry.
Append total % 2 to the result (binary digit).
Update carry = total // 2.
After the loop, reverse the result and return it as a string.
Type	Complexity
Time	O(max(len(a), len(b)))
Space	O(max(len(a), len(b)))"""

