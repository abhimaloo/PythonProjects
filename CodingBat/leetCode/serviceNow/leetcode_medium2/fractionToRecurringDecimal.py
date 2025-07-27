class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: #If the numerator is 0, the result is always "0" regardless of the denominator.
            return "0"

        result = []

        #Uses XOR (^) to determine if the final result should be negative.
        #This ensures that only one (not both) is negative → negative result.
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        # Convert to positive and compute integer part
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))   #Store the integer division.
        remainder = numerator % denominator   #Store the initial remainder to start processing decimal part.

        if remainder == 0:
            return ''.join(result)  #If there's no remainder, you're done

        result.append('.')   #Handle decimal part with repeating detection

        # Use a hashmap (remainder_map) to detect cycles in remainders.
        remainder_map = {}

        #Main loop for decimal expansion
        while remainder != 0:
            if remainder in remainder_map:
                # Insert '(' at the start of repeating part
                idx = remainder_map[remainder]
                result.insert(idx, '(')
                result.append(')')
                break

            remainder_map[remainder] = len(result)
            remainder *= 10   #Multiply the remainder by 10 each time to get the next digit.
            digit = remainder // denominator  #Track when a remainder is repeated — this signals the start of a repeating cycle.
            result.append(str(digit))
            remainder %= denominator

        return ''.join(result)
"""
Example: numerator = 4, denominator = 333

fractionToDecimal(4, 333)
Steps:
Integer part: 4 // 333 = 0
Decimal: repeat starts when remainder = 4, and you get 012012012...
Output: "0.(012)"
| Input                          | Output       |
| ------------------------------ | ------------ |
| `numerator=1, denominator=2`   | `"0.5"`      |
| `numerator=2, denominator=1`   | `"2"`        |
| `numerator=2, denominator=3`   | `"0.(6)"`    |
| `numerator=-50, denominator=8` | `"-6.25"`    |
| `numerator=7, denominator=-12` | `"-0.58(3)"` |



"""