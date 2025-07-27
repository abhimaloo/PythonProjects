#O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            window = (r - l) + 1
            longest = max(longest, window)
            sett.add(s[r])
        return longest

#execution
s = "abcabcbb"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))

"""
l, r = two pointers defining the window (s[l:r])

longest = tracks the maximum length found

sett = stores unique characters in the current window
n = length of the string
If the character s[r] is already in the set:
It means we have a duplicate in the current window.
So, we shrink the window from the left (l) until the duplicate is removed.
Update the longest if this window is the largest so far.
Add s[r] to the set and move to the next character.
Return the length of the longest unique-character substring.
Time Complexity: O(n)
Each character is added and removed at most once from the set → linear time.
📦 Space Complexity: O(min(n, k))
Where k is the character set size (e.g., 26 lowercase letters, or 128 ASCII).

Set stores at most k characters.



"""



