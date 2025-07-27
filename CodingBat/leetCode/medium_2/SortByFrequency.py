from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        # Sort chars by frequency descending
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []
        for char, count in sorted_chars:
            result.append(char * count)

        return "".join(result)


"""

Approach 1: Using a Max Heap or Sorting
Count frequency of each character.
Sort characters by frequency descending.
Build output string accordingly.

Counting: O(n)
Sorting: O(k log k) where k is unique chars

"""