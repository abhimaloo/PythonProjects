class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# Example usage
sol = Solution()
s = ["h", "e", "l", "l", "o"]
sol.reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']