class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0  # open parentheses waiting to be closed
        insertions = 0  # needed insertions

        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1  # match with an open '('
                else:
                    insertions += 1  # unmatched ')', need to add '('

        return insertions + balance


"""
 Intuition:
Use a balance counter:
Traverse the string:
If '(': it increases balance (needs a ) later)
If ')':
If balance > 0 → match it with a previous '('
If balance == 0 → it’s unmatched, we must add '('
At the end:
balance will tell you how many unmatched '(' are left (we need to add ) for them)
Add both unmatched ) and unmatched (

"""