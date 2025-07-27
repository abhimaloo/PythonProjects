class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def distance(c1, c2):
            return min(abs(ord(c1) - ord(c2)), 26 - abs(ord(c1) - ord(c2)))

        res = []
        for ch in s:
            for target in range(26):  # from 'a' to 'z'
                new_char = chr(ord('a') + target)
                cost = distance(ch, new_char)
                if cost <= k:
                    res.append(new_char)
                    k -= cost
                    break  # move to next character
        return ''.join(res)
"""
 Understanding the problem
You’re given:
A string s
An integer k
A distance function that defines a cyclic distance between characters (e.g., 'a' to 'z' is 1)
You want to find the lexicographically smallest string t such that:
distance(s, t) <= k
And you’re allowed to change any character of s to any lowercase letter, any number of times.

🧮 Distance between two characters in cyclic alphabet

def dist(c1, c2):
    return min(abs(ord(c1) - ord(c2)), 26 - abs(ord(c1) - ord(c2)))
✅ Strategy
We want the lexicographically smallest string t, 
while ensuring the total cost (distance between s and t) is ≤ k.
Approach:
Iterate over s from left to right.
For each character s[i], try to change it to the smallest possible character 
'a' to 'z' (in lexicographic order) such that the total cost stays ≤ k.

Deduct the cost from k as we go.


Example
python
Copy
Edit
Input: s = "abc", k = 2

Try to make:
- 'a' → 'a' (cost 0), ok
- 'b' → 'a' (cost 1), k = 1
- 'c' → 'a' (cost 2) → too much
       → 'b' (cost 1), k = 0

Output: "aab"
Time Complexity:
O(n × 26) — worst case, for each character we try up to 26 letters.

"""