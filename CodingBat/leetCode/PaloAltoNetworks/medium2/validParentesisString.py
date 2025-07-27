class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # min open '(' count
        high = 0  # max open '(' count

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low = max(low - 1, 0)
                high -= 1
            else:  # char == '*'
                low = max(low - 1, 0)  # if '*' is ')'
                high += 1             # if '*' is '('

            if high < 0:
                return False  # too many ')'

        return low == 0
"""
Problem Statement:
Given a string s containing only three types of characters: '(', ')', and '*',
return true if s is valid.

Rules for validity:
Every '(' must have a corresponding ')'.
Every ')' must have a corresponding '('.
'*' can be treated as '(', ')', or an empty string.
Key Idea:
Maintain two counters:
low — minimum possible number of open left parentheses.
high — maximum possible number of open left parentheses.
When we see:
'(': increase both low and high by 1 (one more open parenthesis).
')': decrease both low and high by 1 (close one parenthesis).
'*': treat '*' as either '(', ')', or empty:
So, low can decrease by 1 (if '*' is ')' or empty),
high can increase by 1 (if '*' is '(').
Ensure high never drops below 0 (can't have more ')' than '(').
At the end, if low is 0, it means valid matching.
Explanation:
low tracks the least number of open parentheses considering '*' as ')' or empty.
high tracks the most number of open parentheses considering '*' as '('.
If at any point high < 0, it means there are more ')' than '(', invalid.
At the end, if low == 0, all open parentheses can be matched.

Time Complexity:
O(n), single pass through the string.

📦 Space Complexity:
O(1), constant extra space

"""