class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0 ## Left pointer for the position of the next non-zero number

        for r in range(len(nums)):  # r = right pointer
            if nums[r]:  # if the current number is not zero
                nums[l], nums[r] = nums[r], nums[l]  # swap non-zero to front
                l += 1   # move left pointer forward
        return nums   # Not required in-place, but added for clarity


"""
Example
Input:
nums = [0, 1, 0, 3, 12]
Step-by-step:
r = 0: nums[0] = 0 → skip
r = 1: nums[1] = 1 → swap nums[0] and nums[1] → [1, 0, 0, 3, 12], l = 1
r = 2: nums[2] = 0 → skip
r = 3: nums[3] = 3 → swap nums[1] and nums[3] → [1, 3, 0, 0, 12], l = 2
r = 4: nums[4] = 12 → swap nums[2] and nums[4] → [1, 3, 12, 0, 0], l = 3

Final output:

[1, 3, 12, 0, 0]


"""