class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:  #No houses → nothing to rob → return 0.
            return 0
        if len(nums) == 1:
            return nums[0]  #Only one house → just rob it.

        # Dynamic Programming Core
        prev1 = 0  # dp[i - 1]  #max amount we could rob up to previous house.
        prev2 = 0  # dp[i - 2]   #max amount we could rob up to house before previous.

        #Now loop through all houses:
        for num in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + num)
            prev2 = temp

        return prev1
"""
🧠 Key Idea:
Your rob function is solving the classic House Robber problem using 
Dynamic Programming (DP) with constant space. Let’s break it down clearly.
Problem Summary
You're given a list of non-negative integers nums, 
where each element represents the amount of money in a house.
You cannot rob two adjacent houses (i.e., you can't rob both nums[i] and nums[i+1]), 
and your goal is to find the maximum amount of money you can rob
Goal
Return the maximum amount you can rob without triggering the alarm 
(i.e., robbing two adjacent houses).
At each house:
You have two options:
Don't rob it → keep prev1 as is.
Rob it → add current house’s money to prev2 (which is safe because it skips adjacent house).
Pick the maximum of those two options.
Then move your window:
prev2 becomes the old prev1 (saved in temp).
After iterating, prev1 holds the max money you can rob.
Feature	Value
Time Complexity	O(n) — one pass
Space Complexity	O(1) — constant
Technique Used	Dynamic Programming




"""