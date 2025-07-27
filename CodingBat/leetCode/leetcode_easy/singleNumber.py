class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result = n ^ result
        return result


"""
The ^ operator is the bitwise XOR operator.

XOR of two bits is 1 if they are different and 0 if they are the same.

XOR has these important properties:

a ^ a = 0 (XOR of a number with itself is zero)

a ^ 0 = a (XOR of a number with zero is the number itself)


All the numbers that appear twice will cancel each other out because n ^ n = 0.

The number that appears once will remain because XOR with zero keeps the number.

"""