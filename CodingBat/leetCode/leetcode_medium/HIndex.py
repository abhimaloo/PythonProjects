class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations, start=1):
            if c >= i:
                h = i
            else:
                break
        return h
"""
Given an array citations where each element is the number of citations of a researcher's paper, 
compute the researcher's H-index.
The H-index is the largest number h such that the researcher 
has at least h papers with at least h citations each.

Sort the citations in descending order.
Find the maximum h where citations[h-1] >= h.

Explanation:
Sort citations descending: largest first.

Iterate through the sorted list:

i represents the candidate H-index.

Check if citations[i-1] (0-based index) ≥ i.

The largest such i is the H-index.

Time	O(n log n)
Space	O(1) or O(n)


"""