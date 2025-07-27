class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2   #Check if the last bit is 1 (n % 2 is 1 if LSB is 1)
            n = n >>1      # Right shift n to process the next bit
        return res
