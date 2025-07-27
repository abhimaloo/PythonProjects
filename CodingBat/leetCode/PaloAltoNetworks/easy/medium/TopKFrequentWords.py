from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)  # Count word frequencies

        # Build a heap of (-freq, word) to get max-heap behavior
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)

        return result
"""
High-Level Strategy:
Count word frequencies using a dictionary.
Use a heap (priority queue) to track the top k frequent words.
Sort words by:
Frequency (high → low)
Alphabetical order (low → high)
Python's heapq is a min-heap by default.
To simulate a max-heap, we:
Use negative frequencies -freq
Use lexicographical order of word (Python tuples compare element-wise)
This ensures:
Higher frequency = higher priority (because -freq is lower)
If frequencies are equal, smaller word alphabetically comes first





"""