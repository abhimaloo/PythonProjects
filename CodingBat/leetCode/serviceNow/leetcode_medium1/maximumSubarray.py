class Solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)

            if cur_sum < 0:
                cur_sum = 0

        return max_sum


"""

cur_sum: keeps track of the current subarray sum.

max_sum: stores the maximum subarray sum found so far.

If cur_sum becomes negative, we reset it to 0 because continuing with a negative sum 
would reduce the value of any future subarray.

This is an implementation of Kadane's Algorithm 
to find the maximum subarray sum (i.e., the largest sum of a contiguous subarray).


⏱ Time Complexity: O(n)
Single pass over the array (for loop).

Each element is processed exactly once.

📦 Space Complexity: O(1)
Only two variables (cur_sum and max_sum) are used.

No extra space needed based on input size."""