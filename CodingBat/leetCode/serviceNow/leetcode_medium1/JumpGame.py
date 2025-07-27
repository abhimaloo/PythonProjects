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
n is the length of the array.
target is initialized to the last index — our goal is to see if we can reach this from the left.

Loop backward from the last index to the start.

Why backwards?
Because we want to know: "From this position i, can I reach the target?"
If yes, then we update target = i and continue moving left.

At index i, the furthest you can jump is i + nums[i].
If i + nums[i] is enough to reach or pass the target, then we can treat i as a new potential starting point.
So we move the target backward to i.


If after moving from right to left we find that target is now 0, that means we can reach the end starting from index 0.
"""