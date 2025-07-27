class Solution:
    def countDistinct(self, s: str) -> int:
        substrings = set()
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                # Generate substring from i to j
                substr = s[i:j+1]
                substrings.add(substr)

        return len(substrings)
"""
Explanation:
Two nested loops:
i is start index.
j is end index.
Extract substring s[i:j+1] and add to set.
Set automatically keeps only distinct substrings.
Finally, return the count of distinct substrings.
Complexity:
Time: O(n³) due to substring slicing inside nested loops.
Space: O(n²) for storing substrings.
This is the most straightforward brute force method — simple but not efficient for large strings.

"""


    

