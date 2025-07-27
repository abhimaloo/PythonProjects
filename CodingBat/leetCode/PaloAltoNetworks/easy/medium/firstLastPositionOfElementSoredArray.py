class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1  # keep searching on the left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1  # keep searching on the right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        return [findLeft(nums, target), findRight(nums, target)]

"""
 Step-by-Step Explanation:
You use binary search twice:
🔹 1. findLeft() — First Occurrence:
Do binary search.
If nums[mid] == target, record the index and move left to find an earlier match.
Continue until left > right.
🔹 2. findRight() — Last Occurrence:
Same idea, but if nums[mid] == target, record the index and move right.
📦 Return both indices:
If the target was never found, both functions will return -1.
✅ Time and Space Complexity:
Time: O(log n) for each binary search → total O(log n)
Space: O(1) (no extra space used)

Example Walkthrough:
For input:
nums = [5,7,7,8,8,10], target = 8
findLeft() returns 3
findRight() returns 4
Output: [3, 4]




"""