class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []  # will store indices

        for i, temp in enumerate(T):
            while stack and T[stack[-1]] < temp:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)

        return res

"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.


Approach: Monotonic Stack
Key Idea:
Use a stack to keep indices of days with temperatures not yet resolved.
Iterate through the list of temperatures.
For each temperature, pop from the stack while the current temperature is higher than the temperature at the index on top of the stack.
For every popped index, calculate the difference between current index and popped index as the number of days to wait.
Push current day index onto the stack.
Days remaining in stack at the end have no warmer future day, so answer is 0.

Explanation:
The stack stores indices of days with unresolved warmer days.
When a warmer temperature is found, resolve all cooler days in the stack.
The answer for those days is how many days later the warmer temperature occurs.
⏱ Time Complexity:
O(n) — each element pushed and popped at most once.
📦 Space Complexity:
O(n) for stack and output list.
"""