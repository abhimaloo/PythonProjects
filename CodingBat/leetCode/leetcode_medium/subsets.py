class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # to store all subsets
        subset = []   # current subset being built

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())  # store a copy of the current subset
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # # Backtrack: remove nums[i] and explore subset without it
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result


    """
    How it works:
dfs(i) explores all subsets starting from index i.

At each index i, you have two choices:

Include nums[i] in the current subset.

Exclude nums[i] from the current subset.

The recursion explores both paths to generate all possible subsets.

Metric	Value
Time	O(2^n)
Space	O(n) recursion stack + O(2^n) output
    
    """




