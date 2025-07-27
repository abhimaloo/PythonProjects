"""
Given an array nums, rotate the array to the right by k steps, where k is non-negative.
You must do this in-place with O(1) extra space.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # In case k > n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)

        # Step 2: Reverse first k elements
        reverse(0, k - 1)

        # Step 3: Reverse the rest
        reverse(k, n - 1)

"""
🔁 Example:

Input: nums = [1,2,3,4,5,6,7], k = 3  
Output: [5,6,7,1,2,3,4]
Explanation: Rotate right by 3 → the last 3 elements move to the front.
Approach: Three Reversals
The trick is to reverse parts of the array in-place.
Steps:
Reverse the entire array
Reverse the first k elements
Reverse the remaining n - k elements

Why This Works:
Let’s say:


Original:   [1, 2, 3, 4, 5, 6, 7]
Reverse:    [7, 6, 5, 4, 3, 2, 1]
First k:    [5, 6, 7, 4, 3, 2, 1]
Rest:       [5, 6, 7, 1, 2, 3, 4]
✅ Done! This gives us the rotated array.

⏱ Time and Space Complexity:
Time: O(n) — Each element is swapped a few times

Space: O(1) — In-place, no extra array used



"""