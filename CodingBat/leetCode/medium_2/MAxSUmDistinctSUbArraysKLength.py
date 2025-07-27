class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                # shrink window from the left
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum

"""
Approach: Sliding Window + HashSet
Use a sliding window of size k:
Track the elements in the window using a HashSet for uniqueness.
Keep track of:
The current sum.
The start of the window.
The max sum found so far.
If a duplicate is found, shrink the window from the left until all elements are unique.


"""