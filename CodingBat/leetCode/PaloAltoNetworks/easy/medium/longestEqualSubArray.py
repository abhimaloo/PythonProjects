from collections import defaultdict

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        max_len = 0
        positions = defaultdict(list)

        # Step 1: Store indices of each value
        for i, val in enumerate(nums):
            positions[val].append(i)

        # Step 2: For each unique value, use sliding window on its positions
        for val, idxs in positions.items():
            left = 0
            for right in range(len(idxs)):
                # deletions needed = non-matching elements between idxs[left] and idxs[right]
                to_delete = idxs[right] - idxs[left] - (right - left)
                while to_delete > k:
                    left += 1
                    to_delete = idxs[right] - idxs[left] - (right - left)
                max_len = max(max_len, right - left + 1)

        return max_len

"""
The goal is to maximize the number of equal elements in some window after removing at most k others.
Use a sliding window where:
We focus on one target value at a time.
Keep track of how many elements in the current window are not equal to the target → 
those are the ones we would have to delete.

Step 1: Group indexes of each value:
Step 2: Sliding Window for value 3 

Why the formula:
to_delete = idxs[right] - idxs[left] - (right - left)
idxs[right] - idxs[left] → span of the subarray (inclusive)
(right - left) → number of equal values
Subtract to get count of non-equal values in-between (these are the deletions needed)









"""