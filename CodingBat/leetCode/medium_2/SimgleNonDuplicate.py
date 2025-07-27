class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid

        return nums[low]

"""
Approach:
Use binary search between indices low = 0 and high = len(nums) - 1.

Find mid index.

Check if mid is even or odd:

If mid is even:

If nums[mid] == nums[mid + 1] → single element is in right half → low = mid + 2

Else → single element is in left half → high = mid

If mid is odd:

If nums[mid] == nums[mid - 1] → single element is in right half → low = mid + 1

Else → single element is in left half → high = mid - 1

When low meets high, that's the single element.


"""