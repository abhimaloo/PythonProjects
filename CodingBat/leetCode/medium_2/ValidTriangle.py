class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 1, 1, -1):
            left, right = 0, i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count

"""
Problem Statement:
Given an integer array nums, return the number of triplets chosen from the array that can form a valid triangle.
A triangle is valid if for triplet (a, b, c):
a+b>c,b+c>a,c+a>b
Because the array consists of positive integers, it's enough to check:
a+b>c
when the sides are sorted such that 
a≤b≤c.


Approach:
Sort nums.
Iterate i from len(nums)-1 down to 2 (longest side).

Initialize two pointers: left = 0, right = i-1.

While left < right:

If nums[left] + nums[right] > nums[i]:

Count all pairs between left and right → right - left.

Move right one step left.

Else:

Move left one step right.



"""