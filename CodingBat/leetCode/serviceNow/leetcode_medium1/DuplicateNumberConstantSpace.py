
#Solution 1: Floyd’s Tortoise and Hare (Cycle Detection)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: We initialize both slow and fast pointers at the first element. Think of them as runners on the list.
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]  # Move 1 step
            fast = nums[nums[fast]]  # Move 2 steps
            if slow == fast:
                break

        # Phase 2: Find the Entry Point of the Cycle (Duplicate Number)
        slow = nums[0] #Reset slow to the start of the list.
        while slow != fast:
            slow = nums[slow]  #Move both slow and fast one step at a time.
            fast = nums[fast]  #Where they meet again is the duplicate number.

        return slow   #This is the node where the cycle begins — i.e., the duplicate number.

"""
There is a cycle because there’s a duplicate, 
and Floyd’s algorithm helps detect the cycle start, which is the duplicate number.
Time Complexity:
O(n)
📦 Space Complexity:
O(1) — Constant space
This loop detects if there's a cycle.
If a duplicate exists (and it does, by problem constraints), 
the cycle will be entered and the two pointers will eventually meet.


"""

# Solution 2: Binary Search on Value
#Idea:Count how many numbers are <= mid. If more than mid, duplicate is in left half.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            count = sum(num <= mid for num in nums)

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left

"""
 Time Complexity:
O(n log n)

📦 Space Complexity:
O(1)
"""

