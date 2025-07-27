class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1   #n1 should come before n2
            else:
                return 1     # n2 should come before n1

        nums = (sorted(nums, key=cmp_to_key(compare)))  #Uses Python's cmp_to_key from functools to allow custom comparator logic in sorted().


        return str(int("".join(nums)))





"""
Convert all integers to strings so we can concatenate and compare them as strings.
You can’t just sort the numbers numerically.
You need to custom sort them based on string comparison, to maximize the concatenated result.
Time: O(n log n) for sorting

Space: O(n) for string conversion and sorting

"""