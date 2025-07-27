class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False  # odd length strings can't be valid

        low = 0
        high = 0

        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    low += 1
                    high += 1
                else:  # s[i] == ')'
                    low -= 1
                    high -= 1
            else:  # unlocked, can be '(' or ')'
                low -= 1  # if ')'
                high += 1  # if '('

            low = max(low, 0)  # can't have negative open parens

            if high < 0:
                return False  # too many closing parens

        return low == 0

"""
You are given a string s consisting of '(', ')', and '*', and an integer locked of the same length consisting of '0's and '1's.
If locked[i] == '1', the character s[i] cannot be changed.
If locked[i] == '0', the character s[i] can be changed to either '(' or ')'.
Return true if it is possible to make s a valid parentheses string after some (possibly zero)
 changes to the characters where locked[i] == '0'.
A valid parentheses string is one that is either:
Empty,
Can be written as AB (concatenation of two valid parentheses strings), or
Can be written as (A) where A is a valid parentheses string.
✅ Approach: Greedy with Two Counters (Similar to Valid Parenthesis String with '*')
Key Insight:
Like in LeetCode 678 (Valid Parenthesis String), track the possible range of open parentheses.
Use two counters:
low — minimum possible number of open parentheses.
high — maximum possible number of open parentheses.
For each character in s:
If locked and '(': increment both low and high.
If locked and ')': decrement both low and high.
If unlocked (locked[i] == '0'), we can treat it as either '(' or ')', so:
Decrement low by 1 (if changed to ')'),
Increment high by 1 (if changed to '(').
Clamp low to zero since open parentheses cannot be negative.
If at any point high becomes negative, return False.
At the end, if low == 0, the string can be valid.




"""