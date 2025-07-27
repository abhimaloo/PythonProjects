class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * 26  # dp[c] = count subsequences ending with char c
        total = 0

        for ch in s:
            c = ord(ch) - ord('a')
            prev = dp[c]
            dp[c] = (total - prev + 1) % MOD
            total = (total - prev + dp[c]) % MOD

        return total % MOD
