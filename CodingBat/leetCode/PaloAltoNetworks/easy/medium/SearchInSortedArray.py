class Solution:

 def search(self, nums: List[int], target: int) -> int:

    left = 0
    n = len(nums)
    right = n -1

    while left <= right :
        mid = (left + right )//2
        if nums[mid] == target:
            return mid

        # left sorted array
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid -1

                # right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid -1
            else:
                left = mid+1

    return -1

"""
Time complexity:
O(log n) — binary search modified to handle rotation.

space 
O(1) — only variables for indices are used
"""