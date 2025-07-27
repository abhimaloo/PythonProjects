class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]] # Base case: return a list with an empty list

        perms = self.permute(nums[1:])  # Recursively get permutations of the rest
        res = []
        for p in perms:
            for i in range(len(p) + 1):  # Insert the current element at every position
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res

"""
Step-by-Step Explanation
Let’s take an example input: nums = [1, 2, 3]

🔹 Step 1: Base Case
if len(nums) == 0:
    return [[]]
When the input is empty, return a list containing an empty list.
This is used to build up permutations from the ground up.
🔹 Step 2: Recursive Call
perms = self.permute(nums[1:])
This calls the function on the rest of the array, excluding the first element.
For example, if nums = [1, 2, 3], it will first compute permute([2, 3]).
🔹 Step 3: Insert nums[0] into every position of the smaller permutations
Once we get the permutations of [2, 3] → [[2, 3], [3, 2]]
Now we want to insert 1 into every possible position of those:

For [2, 3]:
Insert 1 at index 0 → [1, 2, 3]
Insert 1 at index 1 → [2, 1, 3]
Insert 1 at index 2 → [2, 3, 1]
For [3, 2]:
Insert 1 at index 0 → [1, 3, 2]
Insert 1 at index 1 → [3, 1, 2]
Insert 1 at index 2 → [3, 2, 1]
All 6 permutations are now in res.

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
