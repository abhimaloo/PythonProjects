import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


"""
🧠 Approaches:
✅ 1. Min-Heap (Optimal for k ≪ n) – O(n log k)
Keep a min-heap of size k:
Always store the top k largest elements.
The smallest of the top k is at the root → that’s the kth largest.
"""
"""
2nd solution 
Sort and Return – O(n log n)
Sort the array and pick the kth largest.


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

"""