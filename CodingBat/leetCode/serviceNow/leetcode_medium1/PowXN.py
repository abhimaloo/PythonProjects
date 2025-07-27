class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = abs(n)
        result = 1

        while N:
            if N % 2 == 1:
                result *= x
            x *= x
            N //= 2

        return result if n >= 0 else 1 / result


"""
Core Idea:
Instead of multiplying x n times (which is O(n)), we use divide-and-conquer to reduce the time complexity to O(log n).
Take the absolute value of n, because we'll handle negative exponents at the end.
Initialize result to 1 (multiplicative identity).
If N is odd, multiply result by current x.
Why? Because x^N = x * x^(N-1) when N is odd.

Square x. This reduces the exponent by half in effect:
e.g., if you're computing x^8, instead of multiplying x 8 times, you compute (x^2)^4, then ((x^2)^2)^2, and so on.
Divide N by 2 (integer division).
If original n was positive → return result

If n was negative → return 1 / result


"""


