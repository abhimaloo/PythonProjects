"""
Given an array of integers nums and an integer k, find the total number of continuous subarrays whose sum equals k.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sums = {0: 1}  # Initialize with sum 0 seen once

        for num in nums:
            prefix_sum += num

            # Check if (prefix_sum - k) seen before
            if prefix_sum - k in prefix_sums:
                count += prefix_sums[prefix_sum - k]

            # Record the current prefix_sum count
            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

        return count

"""
Approach: Prefix Sum + Hash Map
Key Idea:
Use a running sum (prefix_sum) while iterating over nums.
At each step, check if there was a previous prefix sum such that:
prefix_sum - previous_prefix_sum = k
Maintain a hashmap (prefix_sums) that stores counts of prefix sums seen so far.
This lets us find how many subarrays ending at current index sum to k efficiently.
Explanation:
prefix_sums keeps track of how many times each prefix sum has occurred.
When prefix_sum - k exists in prefix_sums, it means a subarray summing to k ends at the current index.
Add the count of such prefix sums to count.
Update prefix_sums with the current prefix_sum.
⏱ Time Complexity:
O(n), one pass through the array.
O(n), one pass through the array.
📦 Space Complexity:
O(n), for the hashmap storing prefix sums.




"""