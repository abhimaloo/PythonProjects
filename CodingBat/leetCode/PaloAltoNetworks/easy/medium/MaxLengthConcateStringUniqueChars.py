class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(set(s)) == len(s)  # true if all chars are unique

        def backtrack(index, current):
            nonlocal max_len
            if is_unique(current):
                max_len = max(max_len, len(current))
            else:
                return  # invalid string, stop here

            for i in range(index, len(arr)):
                backtrack(i + 1, current + arr[i])

        max_len = 0
        backtrack(0, "")  #Start exploring combinations from index 0, empty string
        return max_len


"""
Strategy: Backtracking with Set Checks
We explore all combinations (like subset generation) and track used characters.
We backtrack when:

A word itself has duplicates (e.g. "aa")

The combined string would have duplicates

Given an array of strings arr, return the maximum length of a concatenated string with unique characters.

You can:
Choose any subset of strings (including empty set).
Concatenate them in any order.
Only count the length if the final string has no duplicate characters.
Component	Purpose
Backtracking	Explore all string subsets
is_unique()	Validate uniqueness of characters
current + arr[i]	Try next combination
max_len	Track longest valid unique string

"""