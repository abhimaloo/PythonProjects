class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            middle = (left + right) // 2

            if (nums[middle]==target):
                return middle
            elif(nums[middle] > target):
                right = middle - 1
            else:
                left = middle + 1


        return -1




"""
O(log n) — because you divide the problem size by 2 in each step.
"""

