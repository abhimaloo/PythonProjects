class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # update the index of the number

        return False

"""
 Intuition
We want to know if the same number appears again within the last k indices.
This is a classic sliding window with a hash map problem.

How it Works
Iterate through the array.
Store the most recent index of each number in a dictionary.
If the same number is found again and the difference in indices ≤ k, return True.
Time and Space Complexity
Time: O(n)

Space: O(n)


"""