class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):  #We go up to len(nums) - 1 because we don't need to jump after reaching the last index.
            farthest = max(farthest, i + nums[i])   # At every index i, calculate how far we can reach.

            if i == curEnd:
                jumps += 1
                curEnd = farthest

        return jumps

"""
Explanation:
We use a greedy strategy: at every step, we try to jump as far as possible.

📌 Variables:
jumps: how many jumps we've made so far.

curEnd: the farthest index we can reach with the current number of jumps.

farthest: the farthest index we can reach in the next jump.


If we've reached the end of the current jump range, it's time to:
increase the jump count
update the end of the next jump range


Dry Run (nums = [2, 3, 1, 1, 4]):
| i | nums[i] | i + nums[i] | farthest | curEnd | jumps                                      |
| - | -------- | ------------ | -------- | ------ | ------------------------------------------ |
| 0 | 2        | 2            | 2        | 0      | 0    → hit curEnd, jump: jumps=1, curEnd=2 |
| 1 | 3        | 4            | 4        | 2      | 1                                          |
| 2 | 1        | 3            | 4        | 2      | 1    → hit curEnd, jump: jumps=2, curEnd=4 |
| 3 | 1        | 4            | 4        | 4      | 2                                          |
| 4 | 4        | 8            | 8        | 4      | 2                                          |



Done. Reached the end in 2 jumps ✅

🕒 Time and Space Complexity:
Time: O(n) — one pass through the array.

Space: O(1) — only variables used.


"""

