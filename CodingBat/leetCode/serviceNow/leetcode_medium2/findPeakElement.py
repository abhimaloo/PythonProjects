"""
Given an array nums, find a peak element and return its index.
A peak element is one that is strictly greater than its neighbors.

You may assume nums[i] ≠ nums[i+1] for all valid i.
The array may have multiple peaks — you only need to return the index of one peak.
Must solve in O(log n) time (=> binary search hint).
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid  # peak is at mid or to the left
            else:
                left = mid + 1  # peak is to the right

        return left  # or right, since left == right


"""
Set left and right pointers for binary search.

While left is less than right, compute the midpoint.

Compare nums[mid] with nums[mid + 1]:
Case 1: nums[mid] > nums[mid + 1]
This means the slope is descending, so a peak is at mid or before.
So we move right = mid.
Case 2: nums[mid] < nums[mid + 1]
The slope is ascending, so a peak must be after mid.
So we move left = mid + 1.
This always narrows the search toward a peak.
Loop ends when left == right.
That index is a peak element.

 Time and Space Complexity:
Time: O(log n) — binary search

Space: O(1)
"""