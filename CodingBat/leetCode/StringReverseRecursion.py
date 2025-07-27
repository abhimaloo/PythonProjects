class Solution:
    def reverseString(self, s):

        def reverse(l,r):
          if l < r:
             s[l], s[r] = s[r], s[l]
             reverse(l+1,r-1)
        reverse(0, len(s)-1)










# Example usage
sol = Solution()
s = ["h", "e", "l", "l", "o"]
sol.reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']