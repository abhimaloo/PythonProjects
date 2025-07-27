"""
You are given a rotated sorted array of distinct integers (e.g., [4,5,6,7,0,1,2]),
and you need to find the minimum element in O(log n) time.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum must be to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # mid could be the minimum

        return nums[left]


"""
Key Insight:
A rotated sorted array is made by taking a sorted array and shifting it.
Example:
[0,1,2,4,5,6,7] → rotate → [4,5,6,7,0,1,2]
Even though it’s rotated, one part is still sorted, and the minimum is the inflection point (where the order breaks).

Explanation:
Initialize left and right pointers.
While left < right, compute mid.
Compare nums[mid] with nums[right]:
If nums[mid] > nums[right], the minimum is to the right of mid.
Else, the minimum is at mid or to its left, so we move right = mid.
When left == right, that index is the minimum.

⏱ Time Complexity:
O(log n) — classic binary search.
📦 Space Complexity:
O(1) — no extra space used.
Input: [4,5,6,7,0,1,2]

left = 0, right = 6 → mid = 3 → nums[mid]=7 > nums[right]=2 → left = 4
left = 4, right = 6 → mid = 5 → nums[mid]=1 <= nums[right]=2 → right = 5
left = 4, right = 5 → mid = 4 → nums[mid]=0 <= nums[right]=1 → right = 4
Now left == right == 4, so return nums[4] = 0

"""