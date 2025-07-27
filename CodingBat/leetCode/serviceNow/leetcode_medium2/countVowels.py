class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        total = 0

        for i, ch in enumerate(word):
            if ch in vowels:
                total += (i + 1) * (n - i)

        return total
"""
Approach: Contribution Counting
Key Insight:
Instead of generating all substrings (which would be O(n²)), think about the contribution of each vowel character.
Each vowel at index i contributes to many substrings.
The number of substrings containing the character at index i is:
(number of choices for start) * (number of choices for end) = (i + 1) * (n - i)
So the total contribution of vowels is sum over all vowel positions of (i + 1) * (n - i).


 Explanation:
For each vowel, calculate how many substrings include it.

Add all contributions up.

Return the sum.


"""