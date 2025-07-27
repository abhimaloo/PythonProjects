import heapq


class Solution:
    def kClosest(self, points, k):
        minHeap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap) # Converts the list into a min-heap, where the smallest distance is at the top.
        res = []
        while k > 0: # Pop the smallest-distance point from the heap k times.
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res

# Execution
"""Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
"""

solution = Solution()
input = [([[1,3],[-2,2]], 1)]
result = [(points, k, solution.kClosest(points, k)) for points, k in input]
print(result)
"""
Time & Space Complexity:
Time Complexity:

O(n) to build the heap

O(k log n) to pop k items

→ Overall: O(n + k log n)

Space Complexity: O(n) for the heap
"""