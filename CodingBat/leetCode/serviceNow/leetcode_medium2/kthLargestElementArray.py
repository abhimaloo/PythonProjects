import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []  #Create an empty list to use as the heap.
        for num in nums:
            heapq.heappush(min_heap, num)  #Push every number into the heap.
            if len(min_heap) > k:   #If heap size exceeds k, remove the smallest element.
                heapq.heappop(min_heap)    #This ensures that only the k largest elements remain in the heap.
        return min_heap[0]

#After processing all elements,
# the smallest element among the k largest is at the root of the heap → k-th largest.

"""
 Strategy
You use a min-heap of size k to keep track of the k largest elements seen so far.
Why min-heap?
In Python, heapq implements a min-heap.
If we maintain a heap of size k, the smallest among the top k largest elements will be at the top of the heap.
Once we go through all elements, heap[0] will be the k-th largest element.
nums = [3, 2, 1, 5, 6, 4], k = 2
Insert 3 → [3]
Insert 2 → [2, 3]
Insert 1 → [1, 3, 2] → pop 1 → [2, 3]
Insert 5 → [2, 3, 5] → pop 2 → [3, 5]
Insert 6 → [3, 5, 6] → pop 3 → [5, 6]
Insert 4 → [4, 6, 5] → pop 4 → [5, 6]
✅ Final heap: [5, 6] → min_heap[0] = 5 → second largest.



2nd solution 
Sort and Return – O(n log n)
Sort the array and pick the kth largest.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

"""
