class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        result = 0

        while l <= r:
            m = l + ((r - l) // 2)
            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                l = m + 1
                result = m
            else:
                return m
        return result


"""Time Complexity:
O(log x) → binary search reduces the range logarithmically.

Much faster than a linear scan from 0 to x.
"""