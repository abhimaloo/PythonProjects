"""
Given two integers numerator and denominator, return the fraction in string format.
If the fractional part is recurring, enclose the repeating digits in parentheses.
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return ''.join(result)

        result.append('.')  # decimal point

        # Dictionary to store seen remainders and their position in result
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                # Insert '(' at the start of repeating part
                idx = remainder_map[remainder]
                result.insert(idx, '(')
                result.append(')')
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator

        return ''.join(result)

"""
 Key Concepts:
Integer division gives the whole number part.
Remainder gives the fractional part.
To detect repetition in the decimal:
Track remainders you've seen before.
When a remainder repeats, the decimal begins to repeat.

 Explanation:
Handle Sign:

XOR ^ ensures only one of numerator/denominator negative → add -.
Integer Part:
Do numerator // denominator, and update remainder.
Decimal Part (if remainder ≠ 0):
Use a map to record where each remainder first appeared.
Multiply remainder by 10 to simulate long division.
When the same remainder appears again, it means digits are repeating → insert '(' at the first occurrence and append ')' at the end.
🔁 Example Walkthrough: 2 / 3
Integer part: 0
Decimal starts: .
remainder = 2 → 2 × 10 = 20 → 20 ÷ 3 = 6 remainder 2 → repeat starts
So: 0.(6)

"""