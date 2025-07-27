class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find the first index i from the right such that nums[i] < nums[i + 1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the first index j from the right such that nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the suffix starting at i + 1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

"""
Step-by-Step Explanation:
Let’s break it down using this example:
nums = [1, 2, 3, 6, 5, 4]
🔹 Step 1: Find the breakpoint
Find the first index i such that nums[i] < nums[i + 1], scanning from right to left.

In this case:
6 > 5, skip
5 > 4, skip
3 < 6 → so i = 2
If no such index is found (i.e., the array is in descending order), reverse the entire array.

🔹 Step 2: Find the next larger element
From the right side, find the first index j where nums[j] > nums[i]

From right: 4 > 3, so j = 5

🔹 Step 3: Swap nums[i] and nums[j]
Swap nums[2] and nums[5] → [1, 2, 4, 6, 5, 3]

🔹 Step 4: Reverse the suffix from i+1 to end
Reverse elements from index 3 to 5 → [6, 5, 3] becomes [3, 5, 6]

Final result: [1, 2, 4, 3, 5, 6]

✅ Time & Space Complexity:
Time: O(n) — each step involves a linear scan.
Space: O(1) — done in-place.

"""