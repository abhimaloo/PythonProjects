"""
Given an array nums, where each element represents your maximum jump length from that position,
return True if you can reach the last index starting from the first index, otherwise False.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1

        for i in range (n-1, -1, -1):
            max_jump = nums[i]

            if i + max_jump >= target:
                target = i

        return target == 0
"""
We're working backwards from the last index toward the first, 
updating a target that tells us what position we need to reach in order to eventually reach the end.
This method determines if you can jump from index 0 to the last index.
n is the length of the array.
target is initialized as the last index.
The goal is to work backward and see if index 0 can reach this target.
Iterate backward from the last index to the first.
At each position i, max_jump is how far you can jump from there.

If from index i, you can jump to or beyond the current target,
then update target = i.

This means: “If I can jump from i to the place I previously needed to be (target), now I only need to get to i.”
At the end, if we’ve moved the target all the way to index 0,
it means it's possible to reach the end starting from the beginning.
Input: nums = [2, 3, 1, 1, 4]
Start from end: target = 4

i = 4: 4 + 0 >= 4 → target = 4

i = 3: 3 + 1 >= 4 → target = 3

i = 2: 2 + 1 < 3 → target = 3 (unchanged)

i = 1: 1 + 3 >= 3 → target = 1

i = 0: 0 + 2 >= 1 → target = 0

✅ Since target == 0, return True

⏱️ Time Complexity:
O(n) — One pass through the array from end to start.

"""