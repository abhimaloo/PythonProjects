from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Create buckets: index = frequency, value = list of numbers
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        res = []
        # Traverse from highest frequency to lowest
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res




"""

Approach 1: Bucket Sort (Optimal)
🔍 Idea:
Count frequency of each number

Use a bucket where index = frequency, and bucket[i] holds list of numbers with frequency i

Traverse the bucket from the end (most frequent) and collect top k elements

Time Complexity:
O(n) — counting + bucketing + scanning

📦 Space Complexity:
O(n) — hash map + buckets

"""