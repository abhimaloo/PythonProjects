class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        divisor = 1
        while True:
            total = 0
            for num in nums:
                total += math.ceil(num / divisor)

            if total <= threshold:
                return divisor
            else:
                divisor += 1
