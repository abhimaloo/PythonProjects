class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result = n ^ result
        return result

"""
Initially, result is 0.
XOR every number in the list with result.
All duplicates cancel out.
The leftover in result is the single unique number.
How it works:
XOR (^) of a number with itself is 0.
XOR of a number with 0 is the number itself.
XOR is commutative and associative, so all pairs cancel out, leaving only the unique number.
"""