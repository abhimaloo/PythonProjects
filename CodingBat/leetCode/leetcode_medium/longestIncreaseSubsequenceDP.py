class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # Each number is at least a subsequence of length 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

"""

Approach 1: Dynamic Programming (Bottom-Up)
🔍 Idea:
Use a dp array where dp[i] stores the length of the LIS ending at index i.

For each i, check all previous j < i, and if nums[j] < nums[i], then:

python
Copy
Edit
dp[i] = max(dp[i], dp[j] + 1)

Time Complexity:
O(n^2) — nested loop

📦 Space Complexity:
O(n) — for the dp array



"""