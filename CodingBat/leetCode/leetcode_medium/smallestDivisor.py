import math

# binary search
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            total = 0  # renamed from `sum` to avoid shadowing built-in

            for num in nums:
                total += math.ceil(num / mid)

            if total > threshold:
                left = mid + 1
            else:
                right = mid - 1

        return left


#brute force

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        divisor = 1
        while True:
            total = 0
            for num in nums:
                total += math.ceil(num/divisor)

            if total <= threshold:
                return divisor
            else:
                divisor += 1








