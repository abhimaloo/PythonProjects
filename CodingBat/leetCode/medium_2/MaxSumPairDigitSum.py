from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        groups = defaultdict(list)

        for num in nums:
            dsum = sum(int(d) for d in str(num))
            groups[dsum].append(num)

        max_sum = -1
        for group in groups.values():
            if len(group) >= 2:
                group.sort(reverse=True)
                max_sum = max(max_sum, group[0] + group[1])

        return max_sum
"""
Intuition:
For each number, calculate its digit sum.
Group numbers by digit sum.
For each digit sum group, if there are at least 2 numbers, try the top 2 largest numbers and compute their sum.
Keep track of the maximum such pair sum.

Use a dictionary to group numbers by digit sum.
Sort or keep the two largest numbers per digit sum.
Compute max sum from valid groups.
Time = O(n * log n) in the worst case due to sorting each group (can be optimized to O(n))



"""