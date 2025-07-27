class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])


"""
Python's heapq module implements a min-heap, but we need a max-heap to always get the heaviest stone.

So we negate each stone to simulate a max-heap.

Time and Space Complexity:
Time: O(n log n) — each heappop or heappush is O(log n), done at most n times.

Space: O(n) — for the heap storage
"""