import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort meetings by start time
        intervals.sort(key=lambda x: x[0])

        # Min-heap to keep track of end times
        heap = []

        for start, end in intervals:
            # If the earliest ending meeting is done before current starts, reuse that room
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)


"""
 Approach 1: Min Heap (Priority Queue) – Best Choice
 Heap always stores the end times of active meetings.

If a meeting ends before the next one starts, we reuse the room.

The heap size at any time represents the number of rooms currently used.
Time	O(n log n)
Space	O(n)

Sorting: O(n log n)

Heap operations: O(log n) each × n → O(n log n)

 
"""