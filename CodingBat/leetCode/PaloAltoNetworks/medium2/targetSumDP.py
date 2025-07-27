class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total_sum = sum(nums)

        # Check if (S + total_sum) is even and non-negative
        if (S + total_sum) % 2 != 0 or abs(S) > total_sum:
            return 0

        target = (S + total_sum) // 2

        dp = [0] * (target + 1)
        dp[0] = 1  # One way to make sum 0 (empty subset)

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[target]
"""

 Approach: Dynamic Programming (Subset Sum Variation)
Key Insight:
Let P = sum of numbers assigned +

Let N = sum of numbers assigned -

We want: P - N = S
And P + N = sum(nums) → total sum

Add equations: 2P = S + total_sum → P = (S + total_sum) / 2

So, the problem reduces to finding the number of subsets in nums that sum to P.

If (S + total_sum) is not even or P is negative, answer is 0.

Explanation:
dp[j] = number of ways to get sum j.

Iterate through each number and update ways for sums from target down to num.

This avoids double counting subsets.

Time Complexity:
O(n * target), where n = len(nums), target = (S + total_sum) / 2

📦 Space Complexity:
O(target) using 1D DP.



"""