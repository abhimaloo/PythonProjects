from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            i = bisect.bisect_left(products, prefix)

            # Collect up to 3 words starting from index i that start with prefix
            suggestions = []
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
                else:
                    break

            result.append(suggestions)

        return result
"""
 Efficient Approach: Sort + Binary Search
💡Strategy:
Sort the products list lexicographically.
For each prefix of searchWord, use binary search (bisect_left) to find the start index of matching products.
Collect up to 3 matches starting from that index.


Time and Space Complexity:
Time:
Sorting: O(n log n)
For each character in searchWord, binary search: O(log n)
Collecting up to 3 suggestions: O(1)
So overall: O(n log n + m log n), where n = number of products, m = length of searchWord
Space:
O(n) for sorting and result

Lexicographical order is the way words are arranged in a dictionary — i.e., alphabetical order.
It compares words character by character, from left to right, based on the order of letters in the alphabet.
✅ Examples:


"apple" < "banana"
Because "a" comes before "b".


"""