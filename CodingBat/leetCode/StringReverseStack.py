class Solution:
    def reverseString(self, s):
        stack = []
        for c in s:
            stack.append(c)

        i = 0
        while stack:
          s[i] = stack.pop()
          i += 1



# Example usage
sol = Solution()
s = ["h", "e", "l", "l", "o"]
sol.reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']