class Solution:
    def evalRPN(self, tokens):
        stk = []
        for c in tokens:
            if c == "+":
                stk.append(stk.pop() + stk.pop())
            elif c == "-":
               a, b = stk.pop(), stk.pop()
               stk.append(b-a)
            elif c == "*":
                stk.append(stk.pop() * stk.pop())
            elif c == "/":
                a, b = stk.pop(), stk.pop()
                stk.append(int(b / a))
            else:
                stk.append(int(c))
        return stk[0]

# execution
tokens = ["2","1","+","3","*"]
sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))
"""
RPN is a postfix notation: operators come after operands
Stack to keep operands as we parse the tokens.
Addition
Pop two numbers from the stack and add them.
Push the result back.
Sub
a, b = stk.pop(), stk.pop()
stk.append(b - a)
Order matters!

stk.append(stk.pop() * stk.pop())
Pop two numbers, multiply, push result.
Division
a, b = stk.pop(), stk.pop()
stk.append(int(b / a))
Again, order matters: b / a
Use int(b / a) to truncate toward zero 
Convert string to integer and push it to the stack.

After processing all tokens, the result will be the only value left on the stack.

Time: O(n), where n is number of tokens
Space: O(n) for the stack (worst case: all tokens are numbers)





"""