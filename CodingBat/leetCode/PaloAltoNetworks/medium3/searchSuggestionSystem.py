import bisect


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            # Find the insertion point for prefix in products
            i = bisect.bisect_left(products, prefix)

            suggestions = []
            # Check up to 3 products starting at i
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
                else:
                    break
            result.append(suggestions)

        return result


"""
Given an array of strings products and a string searchWord, design a system that suggests at most three product names from products after each character of searchWord is typed.

Suggested products should have a prefix matching the currently typed characters.

If more than three products match, return the three lexicographically smallest.

Return a list of lists of the suggested products after each character is typed.



Approach: Sort + Binary Search
Key Idea:
Sort the products lexicographically.

For each prefix of searchWord, use binary search to find the starting index of products matching the prefix.

Collect up to 3 products starting from that index with the matching prefix.

Return the list of suggestions per prefix.



Explanation:
Sorting ensures suggestions are lexicographically ordered.

Binary search (bisect_left) quickly finds the first product that could match the prefix.

Collect up to 3 products starting from that index.

Repeat for each prefix of searchWord.

⏱ Time Complexity:
Sorting: O(n log n), where n = number of products.

For each prefix (m prefixes), binary search O(log n) + up to 3 checks → O(m log n).

Overall: O(n log n + m log n)

📦 Space Complexity:
O(n) for sorting and output.

"""