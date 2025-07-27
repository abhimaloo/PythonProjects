class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res




"""

Time and Space Complexity
Time Complexity: O(n!)

You generate all n! permutations.

Space Complexity:

O(n!) for storing results +

O(n) for recursion call stack (max depth = n)

O(n!), pronounced "big O of n factorial", 
describes an algorithm whose runtime or 
number of operations grows factorially with the input size n.


"""
