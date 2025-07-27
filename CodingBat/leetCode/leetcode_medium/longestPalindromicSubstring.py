class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLenth = 0
        slenth = len(s)

        for i in range(slenth):
            lp = i
            rp = i
            # odd strings
            while lp >= 0 and rp < slenth and s[lp] == s[rp]:
                if (rp - lp + 1) > resLenth:
                    resLenth = rp - lp + 1
                    result = s[lp:rp + 1]

                lp -= 1
                rp += 1

            lp = i
            rp = i + 1
            # even strings
            while lp >= 0 and rp < slenth and s[lp] == s[rp]:
                if (rp - lp + 1) > resLenth:
                    resLenth = rp - lp + 1
                    result = s[lp:rp + 1]

                lp -= 1
                rp += 1

        return result

"""
result stores the longest palindrome found so far.
resLenth stores its length.
slenth is the length of input string.
Iterate over each character i in the string to treat it as the center of palindrome.
Set two pointers lp (left) and rp (right) starting at i.
Expand outward while characters at lp and rp are equal.
Update result if you find a longer palindrome.
This covers palindromes of odd length (e.g., "aba").

even 
Now set lp at i and rp at i + 1.
Expand outward similarly.
This covers even length palindromes (e.g., "abba").
lp and rp represent two pointers starting at or near the center of a potential palindrome.
lp -= 1 moves the left pointer one step to the left (to check the previous character).

rp += 1 moves the right pointer one step to the right (to check the next character).

Time	O(n²)
Space	O(1)






"""
