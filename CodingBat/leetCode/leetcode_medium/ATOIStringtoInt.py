class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        result = 0

        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for ch in s:
            if not ch.isdigit():
                break
            result = result * 10 + int(ch)
        result = result * sign

        if result < -2 ** 31:
            result = -2 ** 31
        elif result > 2 ** 31 - 1:
            result = 2 ** 31 - 1

        return result

"""
Given a string s, convert it to a 32-bit signed integer with these rules:

Ignore leading whitespace.

Optional + or - sign.

Parse digits until a non-digit character.

Clamp to 32-bit signed integer range [-2^31, 2^31 - 1].

Return the integer result.  
Time	O(n) (one pass through string)
Space	O(1)
"""









