class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i % n]
            if i < n:
                stack.append(i)

        return res


"""
Intuition:
Use a stack to store indices of elements for which we haven't found the next greater element.
We simulate a double pass over the array (since it's circular).
For each index i in [0, 2n-1] (where n = len(nums)), we check:
While current element is greater than element at stack top, pop and update result.
Push current index if it's in the first pass (i < n).

Algorithm Steps:
Initialize an answer array res with -1s.
Use a stack to keep indices of elements waiting for next greater element.
Iterate from 0 to 2 * n - 1 (simulate circular).
For each index i:
While stack is not empty and nums[i % n] > nums[stack[-1]], pop from stack and set res[stack.pop()] = nums[i % n].
If i < n, push i to stack.
Return res.







"""