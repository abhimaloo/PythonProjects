class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2
        return n == 1


    """
    
How It Works:
First, it checks if n is less than or equal to 0 — powers of 2 are always positive, so we return False for negative or 0.

Then it repeatedly divides n by 2 as long as it's divisible by 2.

If at the end, n becomes 1, it means n was a power of 2.

If not, it means there were other prime factors and n was not a pure power of 2.
    
    
    """
