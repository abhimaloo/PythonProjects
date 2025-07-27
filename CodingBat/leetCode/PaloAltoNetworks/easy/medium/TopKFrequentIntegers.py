import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency
        count = Counter(nums)

        # Step 2: Use a heap of size k to get top k elements
        # Python heapq is a min-heap, so we store negative frequency for max-heap behavior
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        # Step 3: Extract top k elements
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
"""
 Approach:
Use a hash map (dictionary) to count frequencies of each element.

Use a heap or sort the frequency map to get the top k frequent elements.

Time Complexity:
Using heap: O(n log k)
Space Complexity:
O(n) for frequency map and heap.

"""