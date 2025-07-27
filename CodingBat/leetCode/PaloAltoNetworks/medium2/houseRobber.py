class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1 = 0  # dp[i - 1]  #max you can rob up to previous house
        prev2 = 0  # dp[i - 2]   #max you can rob up to house before that

        for num in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + num)
            prev2 = temp

        return prev1


"""

🧠 Key Idea:
At each house, you have 2 choices:
Rob the current house → then skip the previous one.
Skip the current house → take whatever max you had until the previous one.
So, at index i, the max money is:
dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
"""