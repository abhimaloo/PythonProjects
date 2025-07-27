import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency
        #This gives a dictionary-like object with the frequency of each number.
        count = Counter(nums)  # Output: {1: 3, 2: 2, 3: 1}

        # Step 2: Use a heap of size k to get top k elements  Build a max-heap
        # Python heapq provides a min-heap, but we simulate a max-heap by using negative frequencies.
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)  #[(-3, 1), (-2, 2), (-1, 3)]

        # Step 3: Extract top k elements
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

"""
Example with k = 2:
First pop: 1 (frequency 3)
Second pop: 2 (frequency 2)
Result: [1, 2]
Time and Space Complexity:
Time Complexity:

O(N log N) for heapify and popping k elements, where N is the number of unique elements.

Space Complexity:

O(N) for the hash map and heap.
Example Run:

nums = [1, 1, 1, 2, 2, 3]
k = 2
Output: [1, 2]




"""