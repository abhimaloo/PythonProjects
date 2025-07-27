class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left_product = 1
        right_product = 1

        # Calculate the product of elements to the left of each element
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]

            # Calculate the product of elements to the right of each element
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result

"""
Given an array nums, return an array result such that:
result[i] = product of all elements of nums except nums[i]
Initialize result array with 1s (so multiplication works without affecting results).
First Pass: Left Products
For each index i, store the product of all elements to the left of i.
left_product keeps track of the cumulative product of nums[0] to nums[i-1].
This builds the prefix product from the left side.

Second Pass: Right Products
Now do a reverse pass to multiply result[i] by the product of elements to the right.
right_product accumulates the product of nums[i+1] to the end.
This completes the result array in place.
Time and Space Complexity:
Metric	Complexity
Time	O(n)
Space	O(1) extra (excluding output array result)

Only two scalar variables (left_product, right_product) used in addition to result.
Total Space Complexity = O(n)
(from the result array)





"""

