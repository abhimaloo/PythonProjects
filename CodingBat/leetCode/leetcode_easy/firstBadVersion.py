# Mocking the isBadVersion API for demonstration purposes
# The isBadVersion API is already defined for you.
# O(log n)time complexity


def isBadVersion(version):
    return version >= 4

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n
        while L < R:
            M = (L + R) // 2
            if isBadVersion(M):
                R = M  # the first bad version is at M or to the left
            else:
                L = M + 1   # first bad version must be to the right
        return L    # or return R, both are same when L == R


# Execution
sol = Solution()
n = 10  # Let's say we have 10 versions
print("First bad version is:", sol.firstBadVersion(n))
