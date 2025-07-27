class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        perm = sorted(nums)

        i = 0  # pointer for nums_sorted
        j = 0  # pointer for perm
        greatness = 0

        while i < len(nums) and j < len(nums):
            if perm[j] > nums_sorted[i]:
                greatness += 1
                i += 1
                j += 1
            else:
                j += 1

        return greatness


"""
Approach:
Sort nums to get the original order.

Create another sorted copy of nums for the permutation.

Use two pointers (i, j) to greedily match each original number nums[i] with the smallest possible number perm[j] that is strictly greater than nums[i].

Count how many matches you can make.
Overall: O(n log n)
"""