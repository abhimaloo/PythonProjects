"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if 'num' is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
"""
Approach:
Key insight:
Use a set for O(1) lookups.
For each number, only try to build the sequence if it is the start of a sequence (i.e., num - 1 is not in the set).
Explanation:
Convert the list to a set to allow O(1) lookups.
Iterate through each number in the set.
If the number is the start of a sequence (num-1 not in set), start counting consecutive numbers.
Keep track of the longest streak found.
Return the longest streak at the end.

Time Complexity:
O(n) — Each number is checked once, and the inner while loop runs only for consecutive sequences, so overall linear time.

Space Complexity:
O(n) for the set.


"""