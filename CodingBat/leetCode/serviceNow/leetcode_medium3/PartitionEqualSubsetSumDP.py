class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False  # can't partition if sum is odd

        target = total // 2
        n = len(nums)

        dp = [False] * (target + 1)
        dp[0] = True  # base case: sum 0 is always possible

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]

"""
✅ Key Insight
If total sum is odd, you can’t split it equally.
If it’s even, your goal is to find a subset whose sum is total // 2.
This becomes a subset sum problem, i.e., can you pick elements that sum to target = total // 2?
🧠 Explanation:
Step 1: Early Exit
if total % 2 != 0:
    return False
Can't divide odd sum equally.

Step 2: Create DP Array
dp = [False] * (target + 1)
dp[0] = True  # sum 0 is always achievable (choose nothing)

Step 3: Update DP Table
for num in nums:
    for i in range(target, num - 1, -1):
        dp[i] = dp[i] or dp[i - num]
        
Iterate backwards to avoid overwriting values used in this round.
dp[i] = True if we can achieve sum i using some subset of numbers.

⏱️ Time and Space Complexity
Metric	Value
Time	O(n * target)
Space	O(target)

Where n = len(nums) and target = total_sum // 2

"""