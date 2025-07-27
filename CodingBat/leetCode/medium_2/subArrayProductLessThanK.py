class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        left = 0
        result = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            result += right - left + 1

        return result
"""
Use a sliding window approach with two pointers left and right.
Maintain the product of elements in the current window.
Expand right pointer, multiply product by nums[right]
While product >= k, move left pointer forward and divide out nums[left].
The number of new valid subarrays ending at right is (right - left + 1).
✅ Why (right - left + 1)?
Because every subarray ending at right and starting anywhere between left and right is valid.


"""