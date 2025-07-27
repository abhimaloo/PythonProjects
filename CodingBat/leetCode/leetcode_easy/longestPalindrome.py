from collections import defaultdict
#Time Complexity: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        result = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                result += 2

        for value in count.values():
            if value % 2 == 1:
                result += 1
                break

        return result








# Execution

sol = Solution()

print(sol.longestPalindrome("a"))






