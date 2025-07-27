class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # Step 1: Shift result left to make room
            res = (res << 1)

            # adds the rightmost bit of n to the result
            res = res | (n & 1)

            # shift the n to right to get the next bit
            n = n >> 1

        return res


"""
You're processing the input n bit-by-bit, from right to left.

At each step:

res << 1: Makes room for the next bit in res (i.e., shifts all bits to the left).

n & 1: Extracts the rightmost bit of n.

res | (n & 1): Adds that bit to res.

n >> 1: Moves to the next bit of n.
"""