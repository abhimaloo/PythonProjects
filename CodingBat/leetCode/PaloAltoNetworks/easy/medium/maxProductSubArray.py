class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max, curr_min = 1, 1

        for num in nums:
            if num == 0:
                curr_max, curr_min = 1, 1
                continue

            temp = curr_max * num
            curr_max = max(num, temp, curr_min * num)
            curr_min = min(num, temp, curr_min * num)

            res = max(res, curr_max)

        return res

"""
The Maximum Product Subarray problem is a classic dynamic programming problem where you're asked to 
find the contiguous subarray (containing at least one number) that has the largest product.

Why it's tricky:
Unlike sum, product is sensitive to signs (negative × negative = positive).

A negative number can flip a max product into a min, and vice versa.

So, you need to track both max and min products at each index.


For each element in the array:

Keep track of:

max_so_far: the maximum product ending at this position.

min_so_far: the minimum product ending at this position.

Swap max_so_far and min_so_far if current number is negative.

Let’s break that down:

We calculate temp = curr_max * num because curr_max will change in the next line.

curr_max becomes the maximum among:

num (start fresh at this number),

curr_max * num (extend previous max),

curr_min * num (maybe current number is negative, so multiplying a big negative becomes a large positive).

curr_min is calculated similarly



"""