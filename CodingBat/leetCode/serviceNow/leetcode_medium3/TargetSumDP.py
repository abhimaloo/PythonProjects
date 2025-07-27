from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # Check if the transformed subset sum target is valid
        if (target + total) % 2 != 0 or total < abs(target):
            return 0

        subset_sum = (target + total) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # One way to make sum 0: use nothing

        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]

"""
Problem Summary
You are given an integer array nums and an integer target.
You can add either '+' or '-' before each number.
Return the number of ways to assign symbols to make the sum equal to target.
✅ Approach 1: Dynamic Programming with Subset Sum Transformation
💡 Key Insight:
We can transform this into a Subset Sum problem.
Let:
P = sum of numbers with +
N = sum of numbers with -

P - N = target       (1)
P + N = totalSum     (2)
Add both:

2P = target + totalSum ⟹ P = (target + totalSum) // 2
So the problem becomes:
Find the number of subsets in nums that sum to P = (target + totalSum) // 2
🚨 Constraint:
If (target + totalSum) is odd or target > totalSum, there is no solution.
✅ Example Dry Run:
For nums = [1,1,1,1,1], target = 3:
total = 5
subset_sum = (3 + 5) // 2 = 4
We count number of subsets that sum to 4
Result: 5 subsets

"""