class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x: float, n: int) -> float:
            if n == 0:
                return 1.0
            half = power(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1 / power(x, -n)
        else:
            return power(x, n)

"""
Step-by-step Explanation:
Base case:
if n == 0:
    return 1.0
Any number raised to power 0 is 1.
Recursive case:
half = power(x, n // 2)
Recursively compute x^(n//2).
Combine results:
If n is even:
x^n = (x^(n//2)) * (x^(n//2)) = half * half
If n is odd:
x^n = (x^(n//2)) * (x^(n//2)) * x = half * half * x
Handle negative powers:
if n < 0:
    return 1 / power(x, -n)
    
Example:
x = 2.0, n = 10

myPow(2.0, 10)

Calls power(2.0, 10)

Breaks down recursively: power(2.0, 5) → power(2.0, 2) → power(2.0, 1) → power(2.0, 0)

Then builds back up with squaring and multiplying as needed.

⏱️ Time Complexity:
O(log n) — due to recursive halving of n.

"""


