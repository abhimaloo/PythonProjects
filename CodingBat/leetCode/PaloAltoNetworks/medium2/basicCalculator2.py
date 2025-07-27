class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        stack = []
        num = 0
        sign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            # If char is operator or at the end of string
            if char in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    last = stack.pop()
                    # Integer division toward 0
                    stack.append(int(last / num))

                sign = char
                num = 0

        return sum(stack)
"""
Problem Statement:
Implement a basic calculator to evaluate a simple expression string containing:
Non-negative integers
Operators: +, -, *, /
No parentheses
Respect operator precedence (* and / before + and -)
Integer division truncates toward zero

Approach: Stack + One Pass
Key Idea:
We process the string left to right, tracking the current number and the last operator.
Use a stack to store numbers.
On + or -, push the number (positive or negative).
On * or /, pop the last number, compute, then push result.
At the end, sum the stack.

 How It Works:
For input: "3+2*2"
Read 3, sign is '+' → stack = [3]
Read 2, sign is '+' → wait
Read *, apply previous sign (+ 2) → stack = [3, 2], new sign = *
Read 2, apply * → pop 2, 2 * 2 = 4 → stack = [3, 4]
Sum = 3 + 4 = 7
⏱ Time & Space Complexity:
Time: O(n) — one pass
Space: O(n) for the stack

"""