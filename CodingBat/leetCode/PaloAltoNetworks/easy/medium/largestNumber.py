from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = (sorted(nums, key=cmp_to_key(compare)))
        return str(int("".join(nums)))


"""
Given nums = [3, 30, 34, 5, 9], return the largest concatenated number as a string:
✅ Output: "9534330"
Convert all integers in the list to strings because we’ll need to concatenate them and compare string combinations.
Custom Comparator Function:
This function defines how to sort two strings.
Suppose n1 = "3" and n2 = "30":
Compare "330" vs "303"
Since "330" > "303", "3" should come before "30"
We return -1 if n1+n2 should come before n2+n1
Custom Sorting:
nums = (sorted(nums, key=cmp_to_key(compare)))
Use cmp_to_key from functools to convert our compare function into a key function.
This sorts the list using our custom rule.
Concatenate the sorted strings into one big number.
Convert it to int first to remove leading zeroes, then back to str.

This also handles edge cases like [0, 0, 0] → "0" not "000"


"""


