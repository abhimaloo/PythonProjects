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
Approach: Recursive Backtracking (Insertion Based)
This function uses recursion to generate all permutations by: Breaking down the list step by step.
Inserting the current number at every possible position in all permutations of the smaller list.

Base case: If the list is empty, the only permutation is an empty list [].
So, we return [[]].
We recursively call permute on the list without the first element, i.e., nums[1:].
This gives us all permutations of the smaller sublist.

For each permutation p of the smaller sublist:
We insert the first number (nums[0]) at every possible position.
Then we add that new permutation to the result.



Time and Space Complexity
Time: O(n × n!)
Because there are n! permutations, and copying/inserting in a list of length n takes O(n).
Space: O(n!) for storing results, and O(n) call stack depth.

O(n!), pronounced "big O of n factorial", 
describes an algorithm whose runtime or 
number of operations grows factorially with the input size n.


"""
