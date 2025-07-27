roughly = o(2**n)
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranetheses when open < n
        # only add closed paratheses when closed < open
        # valid when open==closed== n

        stack = []
        result = []

        def backtracking(openN, closedN):  #If we’ve added n open and n close, the string is complete and valid.
            if openN == closedN == n:  #Base case:
               result.append("".join(stack))   #Convert the stack list to a string and store it in result.
               return

            if openN < n:      #➕ Case 1: Add ( if openN < n
                stack.append("(")
                backtracking(openN + 1, closedN)  #Recurse with openN + 1
                stack.pop()     #After the recursive call, we pop to backtrack and try other options.

            if closedN < openN:   #➕ Case 2: Add ) if closedN < openN
                stack.append(")")
                backtracking(openN, closedN + 1)
                stack.pop()

        backtracking(0, 0)
        return result

"""
Backtracking is a problem-solving technique that utilizes recursion to systematically
 explore all possible solutions to a problem by building up a solution step-by-step and abandoning 
(or backtracking from) invalid or undesirable paths as soon as they are detected
 Time and Space Complexity
Time: O(2^2n) (worst case, exponential due to recursion)

But we only build valid sequences → so it's more efficient than brute force

Space: O(n) recursion depth + O(n) for stack
stack: temporary list to build one valid string
result: list of all valid combinations

🔁 Example Walkthrough (n = 2)
Let's trace it:

Initial Call:

backtracking(0, 0)
→ Add '(':

stack = ['(']
backtracking(1, 0)
→ Add '(' again:


stack = ['(', '(']
backtracking(2, 0)
→ Now we can't add ( (openN == n), so add ')':
stack = ['(', '(', ')']
backtracking(2, 1)
→ Add ')' again:
stack = ['(', '(', ')', ')']
backtracking(2, 2)
✅ Base case hit → add "(())" to result.

Then backtrack...
→ From ['(', '('], try ['(', ')']:


stack = ['(', ')']
backtracking(1, 1)
→ Add '(' again:

stack = ['(', ')', '(']
backtracking(2, 1)
→ Add ')':
stack = ['(', ')', '(', ')']
backtracking(2, 2)
✅ Base case hit → add "()()" to result.

🧪 Final Output for n = 2
python
Copy
Edit
["(())", "()()"]
⏱ Time & Space Complexity
Time: O(2ⁿ) — each position has up to 2 choices (( or )), but pruning keeps it lower than brute force.

Space: O(n) for the stack during recursion. 




"""


