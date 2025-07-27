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
What You Did Right:
✅ Used Counter to count word frequencies.
✅ Built a heap using (-freq, word) to simulate max-heap behavior.
✅ Correctly used heapq.heappop() to extract the top k frequent words.

⚠️ Edge Case Issue:
Python’s heapq sorts tuples by:
First element (frequency in this case)
Then second element (word), in ascending (alphabetical) order if frequencies are equal.
That works only if you want ties to be resolved alphabetically (which you do in this problem) — 
and you already handle that properly! 🥳

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

Output: ["i", "love"]
Time and Space Complexity:
Time:
O(N log N) for heapify and k pops (N is number of unique words)

Space:
O(N) for Counter and heap



"""