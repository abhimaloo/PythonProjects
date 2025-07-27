"""
You are given a character array s, representing a string of words separated by spaces.
You must reverse the words in place, i.e., without allocating extra space for another array.
"""

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        # Step 1: Reverse the entire list
        reverse(0, len(s) - 1)

        # Step 2: Reverse each word
        start = 0
        for end in range(len(s) + 1):
            if end == len(s) or s[end] == ' ':
                reverse(start, end - 1)
                start = end + 1
"""
Approach:
Reverse the entire array
Reverse each word individually
This works because:
Reversing the whole array puts words in the correct order but with letters reversed.
Reversing each word fixes the order of letters in each word.
🧠 Step-by-Step:
Given: "the sky is blue"
Step 1: Reverse entire string → "eulb si yks eht"
Step 2: Reverse each word:
"eulb" → "blue"
"si" → "is"
"yks" → "sky"
"eht" → "the"
Final result: "blue is sky the"



"""