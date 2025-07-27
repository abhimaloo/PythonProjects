from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for c in s:
            count[c] += 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1


"""Problem Statement:
You are given a string s. 
You need to find the index of the first non-repeating character in it. 
If no such character exists, return -1.
defaultdict(int) creates a dictionary that defaults to 0 for any new key.
This will be used to count the frequency of each character in the string.

Loop through each character in the string s.
Increment the count of that character in the dictionary.
After this loop, count will hold how many times each character appears.
This loop goes through the string again, 
but now using enumerate() to get both index i and character c.
It checks: If the count of that character is 1, it means it's the first non-repeating character.
Return its index immediately.
If no character with a count of 1 was found in the loop above, return -1.
This is a two-pass solution:
First pass counts character frequency.
Second pass finds the first character with frequency 1

Time Complexity: O(n)
📦 Space Complexity: O(1)


Same logic via regular map 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # First pass: count each character
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        # Second pass: find the first character with count 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1

"""

