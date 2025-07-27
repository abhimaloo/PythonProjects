class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i]) # Explore current index (include and exclude):
            dfs(i, curr, total + candidates[i])
            curr.pop() # Then backtrack using curr.pop() to remove last element.

            dfs(i + 1, curr, total)  #Exclude current number:

        dfs(0, [], 0) # Start recursion from index 0 with empty path and total sum = 0.
        return result
"""
Given a list of distinct integers candidates and a target integer target,
Return all unique combinations where the candidate numbers sum to target.
You can reuse the same number multiple times.
Explanation Step-by-Step:
### 🔁 dfs(i, curr, total) is a recursive function:
i: current index in the candidates array.
curr: the current list of numbers being added together.
total: the current sum of numbers in curr.
Base cases:
if total == target:
    result.append(curr.copy())
    return
If the total matches the target, we found a valid combination.
curr.copy() is used to store the current path, because curr is a mutable list.
if i >= len(candidates) or total > target:
    return
If the index goes out of bounds or total exceeds target, stop recursion.

🔹 Recursive choices:
curr.append(candidates[i])         
dfs(i, curr, total + candidates[i])
curr.pop()
Include the current number candidates[i]

Stay at the same index (i) so the number can be used again.

After exploring that path, backtrack using curr.pop().
dfs(i + 1, curr, total)
Exclude the current number and move to the next index (i + 1).

Example Dry Run:
Input: candidates = [2, 3, 6, 7], target = 7

Start from dfs(0, [], 0):

Include 2 → [2], total = 2

Include 2 again → [2, 2], total = 4

Include 2 again → [2, 2, 2], total = 6

Include 2 again → [2, 2, 2, 2], total = 8 → too much → backtrack

Exclude 2, try 3 → [2, 2, 3] → total = 7 → valid!

Backtrack and try other combinations...

Eventually finds:

[[2, 2, 3], [7]]

Time and Space Complexity:
Time Complexity: Exponential O(2^T) where T is the target, because for each number we can choose include/exclude.

Space Complexity: O(T) recursion depth, and results stored.




"""




