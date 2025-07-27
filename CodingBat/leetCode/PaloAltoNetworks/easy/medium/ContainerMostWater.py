class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            result = max(area, result)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result

"""
Initialize two pointers: l (left) and r (right).
result keeps track of the maximum area found so far.
Calculate the area between height[l] and height[r].

Update the result if this area is larger.

Always move the shorter line inward.

Why? Because moving the taller line won't increase the height, and reducing width will decrease area. 
But moving the shorter line might give a taller line (and possibly more area).

Time: O(n) — Each element is visited once.

Space: O(1) — No extra space used.
"""