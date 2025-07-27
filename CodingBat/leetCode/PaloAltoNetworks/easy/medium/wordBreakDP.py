class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # for O(1) lookup
        n = len(s)
        dp = [False] * (n + 1)  #So we need to go from 0 to n (inclusive) → hence n + 1 elements.
        dp[0] = True  # empty string is always breakable

        for i in range(1, n + 1):   # ending index of substring
            for j in range(i):       # starting index of candidate word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


"""
You're given: A string s
A list of strings wordDict
Your task:
Return True if s can be segmented into space-separated words from wordDict, else return False.
✅ Key Idea: Dynamic Programming
We use a boolean array dp where:
dp[i] is True if s[0:i] can be segmented using words from the dictionary.
🧱 Intuition:
At every position i, check if there is a word in wordDict that ends at position i, 
and the substring before it is breakable.
Use Dynamic Programming to build up breakability from left to right.
Use a set for fast wordDict lookup.
Efficient and widely accepted solution.

Time	O(n²) where n = len(s)
Space	O(n) for the dp array

"""
