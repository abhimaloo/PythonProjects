class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s = list(s)

        while l < r:
            while not s[l].isalpha() and l < r:
                l += 1
            while not s[r].isalpha() and l < r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)

