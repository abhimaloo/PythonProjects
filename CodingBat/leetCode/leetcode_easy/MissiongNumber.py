class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += (i - nums[i])
        return result


"""
Initialize result = len(nums) — this represents the last number n in the range [0, n].

Loop through all indices and subtract the values:

This is equivalent to:


result = sum(0 to n) - sum(nums)
Which correctly gives the missing number.

"""