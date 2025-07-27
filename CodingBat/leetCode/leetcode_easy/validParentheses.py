# time cmplexity o (n)

class Solution:
    def isValid(self, s: str) -> bool:
        openBracketsStack = []
        closingBracketsMappping = {')':'(', '}':'{', ']':'['}
        for p in s :
            if p in closingBracketsMappping.values():
               openBracketsStack.append(p)
            elif openBracketsStack and closingBracketsMappping[p] == openBracketsStack[-1]:
               openBracketsStack.pop()
            else:
               return False
        return openBracketsStack == []

"""
We use a stack to track open brackets.

A map defines the matching pairs for closing brackets.

Case 1: Open Bracket = Push open brackets ((, {, [) onto the stack.
Case 2: Closing Bracket = Check if the top of the stack is the matching open bracket.
If yes, pop it — it's a valid pair.

Case 3: Invalid Bracket
return openBracketsStack == [] If the stack is empty, all brackets were matched correctly.
If not, it means there are unmatched open brackets left → return False.
You go through each character in the string once: O(n)

Each push and pop on the stack takes O(1) time

So overall: O(n)



"""