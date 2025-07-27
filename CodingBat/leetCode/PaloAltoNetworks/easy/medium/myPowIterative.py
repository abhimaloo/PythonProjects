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
Defines a method myPow that takes:
a float x (the base),
an integer n (the exponent).
Handles negative exponents by working with the absolute value of n.
We'll deal with the sign at the end.
Initialize the result to 1, which is the multiplicative identity.

If N is odd, multiply result by current x.
(Because x^n = x * x^(n-1) when n is odd.)
Square x → this reduces the number of multiplications.
Halve N (integer division).
This is the key idea of exponentiation by squaring:
Reduces time complexity from O(n) to O(log n).
If the original n was negative, invert the result to get the correct value.

"""

