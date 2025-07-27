from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for count in freq.values():
            if count % 2 != 0:
                return False

        return True


"""
 Key Insight
To pair each number with an identical one, each number must appear an even number of times.
Approach
Count the frequency of each number using a hashmap (or collections.Counter).

For each number, check if its count is even.

If all counts are even → return True, else False.
Time and Space Complexity
Time: O(n), where n is the number of elements in nums

Space: O(n), for storing the count in a dictionary

"""