class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp

"""

Explanation:
i >> 1: This is i // 2 (integer division by 2).

i & 1: This gives 1 if the least significant bit of i is 1, otherwise 0.
dp[i] = dp[i // 2] + (i % 2)
This works because:

i // 2 has already been computed in a previous step.

We build the result bottom-up, starting from 0.

"""