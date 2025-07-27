class Solution:
    def mergeSortedArray(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # merge all nums 2 element in nums1
        while n > 0:
            nums1[last] = nums2[n - 1]
            last -= 1
            n -= 1


"""
last points to the last index of nums1 (where the largest merged value will go).
We're merging from the back to avoid overwriting values in nums1.
As long as both arrays have values left:
Compare nums1[m-1] and nums2[n-1]
Place the larger one at index last
Decrease the pointer (m or n) and move last back
This ensures the largest remaining value goes to the right spot.
If nums1 is exhausted (m == 0) but nums2 still has elements, copy them over.
No need to copy remaining elements from nums1, because they’re already in place.

Time Complexity:
O(m + n) → each element is visited once.

📦 Space Complexity:
O(1) → done in-place, no extra space.

"""