class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # If total sum is odd, can't split equally
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        # dp[i] = True if sum i can be formed using some elements
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Traverse backwards to avoid using the same number multiple times
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True

        return dp[target]
"""
Approach: Dynamic Programming (Subset Sum Problem)
Key Insight:
The problem reduces to checking if there is a subset with sum equal to total_sum / 2.

If total sum is odd, return False immediately.

Otherwise, use a DP approach to find if such subset exists.

🔧 Steps:
Calculate total_sum.

If total_sum is odd, return False.

Set target = total_sum // 2.

Use a boolean DP array to track if sums are achievable.

Iterate through numbers and update possible sums.


Explanation:
dp[0] = True means zero sum is always possible (empty subset).

For each number, update dp array to mark achievable sums.

If dp[target] is True after processing all numbers, it means there's a subset summing to target.

⏱ Time Complexity:
O(n * target), where n is length of nums and target = total_sum / 2.

📦 Space Complexity:
O(target) using 1D DP optimization.

"""